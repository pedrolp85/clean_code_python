@dataclass
class AwsMarketPlaceGenerator:
    start_date: str
    resource_id: str
    product_sku: str
    region: str
    product_name: str
    legal_entity: str
    amount: int
    rate: int
    tags: Dict[str, str]


@dataclass
class AwsHcsMockData:

    lineitem_resourceid: str
    lineitem_availabilityzone: str
    product_region: str
    resourcetags: Dict[str, str]
    product_productname: str
    lineitem_usageamount: float
    lineitem_unblendedrate: float
    lineitem_blendedrate: float
    lineitem_unblendedcost: float
    lineitem_blendedcost: float
    pricing_publicondemandcost: float
    ebs_account_id: int
    org_id: int
    source: str
    bill_payeraccountid: str
    lineitem_usageaccountid: str
    month: int
    year: int
    lineitem_usagestartdate: str
    bill_billingentity: str = "AWS Marketplace"
    pricing_unit: str = "Hrs"
    lineitem_currencycode: str = "USD"
    lineitem_productcode: str = "5hnnev4d0v7mapf09j0v8of0o2"
    lineitem_legalentity: str = "Red Hat"

    def __init__(
        self,
        source_uuid: str,
        user: str,
        payer: str,
        aws_generator: AwsMarketPlaceGenerator,
        identity: Dict[str, str],
        day: int,
        month: int,
        year: int,
    ):

        self.lineitem_resourceid = (
            f"arn:aws:ec2:{aws_generator.region}:{payer}:instance/i-{aws_generator.resource_id}"
        )
        self.lineitem_availabilityzone = aws_generator.region
        self.product_region = aws_generator.region[:-1]
        # hcs file is us-east-1 withour final 'a'
        self.product_productname = aws_generator.product_name
        self.lineitem_usageamount = float(aws_generator.amount)
        self.lineitem_unblendedrate = self.lineitem_blendedrate = float(aws_generator.rate)
        self.lineitem_unblendedcost = (
            self.lineitem_blendedcost
        ) = self.pricing_publicondemandcost = float(aws_generator.rate * aws_generator.amount)

        resource_tags = {}

        for key, value in aws_generator.tags.items():
            resource_tags.update({key.replace("resourceTags/user:", ""): value})

        self.resourcetags = resource_tags
        self.ebs_account_id = int(identity.get("account_number", False))
        self.org_id = int(identity.get("org_id", False))
        self.source = source_uuid
        self.bill_payeraccountid = payer
        self.lineitem_usageaccountid = user
        self.lineitem_usagestartdate = day
        self.month = month
        self.year = year

    def compare_with_panda(self, panda_row: pd.DataFrame, hours) -> bool:
        # compare self instance with a panda row of data from a hcs csv
        # the eq condition for some fields cannnot be assert only with ==

        unfinished_calculations = [
            "lineitem_usageamount",
            "lineitem_unblendedcost",
            "lineitem_blendedcost",
            "pricing_publicondemandcost",
        ]

        substring_matching = ["lineitem_legalentity", "lineitem_usagestartdate"]

        for column in self.__dataclass_fields__:

            if column in unfinished_calculations:
                if panda_row[column] != getattr(self, column) * hours:
                    return False, {
                        "field": column,
                        "expected": getattr(self, column) * hours,
                        "found": panda_row[column],
                        "operator": "eq",
                    }

            elif column in substring_matching:
                if getattr(self, column) not in panda_row[column]:
                    return False, {
                        "field": column,
                        "expected": getattr(self, column),
                        "found": panda_row[column],
                        "operator": "in",
                    }

            elif column == "resourcetags":
                if getattr(self, column) != json.loads(panda_row[column]):
                    return False, {
                        "field": column,
                        "expected": getattr(self, column),
                        "found": panda_row[column],
                        "operator": "in",
                    }

            else:
                if panda_row[column] != getattr(self, column):
                    return False, {
                        "field": column,
                        "expected": getattr(self, column),
                        "found": panda_row[column],
                        "operator": "eq",
                    }

        return True, None







def test_api_aws_hcs_dataclass_poc_report_content(
    application, cost_aws_source_static, cost_boto3_session_minio, tmp_path
):
    """POC with HCS file mocking

    metadata:
        requirements: cost_hcs
    """

    if application.config.current_env in ["local"]:

        source_uuid = cost_aws_source_static.uuid

        today = get_manifest_modified_datetime(application, source_uuid)
        previous_month_end = get_date(n_months_ago=2, day=31)  # get last day of previous month

        s3_resource, s3_client, real_bucket = cost_boto3_session_minio

        data, accounts = read_marketplace_data_to_dataclass("aws_static_report_basic.yml")

        # get HCS files data

        hcs_files = wait_for_hcs_reports(
            real_bucket, source_uuid, files_to_check=[previous_month_end, today]
        )

        days_to_check = get_day_sample(application, today=today)
        selected_files = [
            file_path
            for file_path in hcs_files
            if file_path.split("hcs_")[-1].strip(".csv") in days_to_check
        ]

        for file_path in selected_files:
            hcs_file_name = file_path.split("/")[-1]
            downloaded_file = f"{tmp_path}/{hcs_file_name}"
            LOG.info(f"Downloading file {file_path}")
            s3_client.download_file(
                Bucket=real_bucket.name, Key=file_path, Filename=downloaded_file
            )

            LOG.info(f"Loading {downloaded_file}")

            day, month, year, hours = get_date_info_from_hcs_file_name(hcs_file_name, today)

            LOG.info(f"Verifying the content of {hcs_file_name}")

            hcs_mock_line_item = [
                AwsHcsMockData(
                    source_uuid,
                    accounts.get("user")[0],
                    accounts.get("payer"),
                    gen,
                    application.user.identity,
                    day,
                    month,
                    year,
                )
                for gen in data
            ]

            df = pd.read_csv(downloaded_file)

            assert (
                df.shape[0] == 2
            ), f"Unexpected number of items in the file - {df.shape[0]} instead of 2"

            panda_row = 0

            for item in hcs_mock_line_item:
                # compare data in generator basis with every panda csv line
                assertion_result, metadata = item.compare_with_panda(df.iloc[panda_row], hours)
                panda_row += 1
                assert (
                    assertion_result
                ), f"failed assertion for field {metadata ['field']} in file {hcs_file_name},"
                f"expected {metadata['expected']} {metadata['operator']}, {metadata['found']}"



def read_marketplace_data_to_dataclass(yaml_file_name):

    input_file = find_data_file(yaml_file_name, "cost_management")
    with open(input_file) as file_obj:
        yaml_file = yaml.safe_load(file_obj)
        accounts = yaml_file.get("accounts", {})
        # Get data for Red Hat Marketplace items
        rh_marketplace_items = []

        if "aws" in yaml_file_name.lower():

            rh_marketplace_items = [
                AwsMarketPlaceGenerator(**generator["MarketplaceGenerator"])
                for generator in yaml_file["generators"]
                if list(generator.keys())[0] == "MarketplaceGenerator"
                and "Red Hat" in generator["MarketplaceGenerator"].get("legal_entity", [])
            ]

    accounts = yaml_file.get("accounts", {})
    return rh_marketplace_items, accounts


def get_date_info_from_hcs_file_name(file_name, today, provider="aws"):

    day = file_name.strip("hcs_ | .csv")
    month = int(day[5:7])
    year = int(day[:4])
    hours = today.hour if day == today.strftime("%Y-%m-%d") else 24

    return day, month, year, hours