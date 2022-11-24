import random
from dataclasses import dataclass, field
from typing import Dict, List
import pandas as pd
import yaml


@dataclass
class Person:
        id: int
        name: str
        age: int


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
    tags: Dict[str,str]


@dataclass 
class AwsHcsMockData():
    
    lineitem_resourceid: str
    lineitem_availabilityzone: str 
    product_region: str 
    resourcetags: Dict[str,str] 
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


    def __init__(self, source_uuid: str, user:str, payer:str , aws_generator: AwsMarketPlaceGenerator, identity: Dict[str, str] , day: int, month: int, year: int):
       
        self.lineitem_resourceid =  f"arn:aws:ec2:{aws_generator.region}:instance/i-{aws_generator.resource_id}"
        self.lineitem_availabilityzone = aws_generator.region
        self.product_region = aws_generator.region[:-1]
        self.product_productname = aws_generator.product_name
        self.lineitem_usageamount = float(aws_generator.amount)
        self.lineitem_unblendedrate = self.lineitem_blendedrate = float(aws_generator.rate)
        self.lineitem_unblendedcost = self.lineitem_blendedcost = self.pricing_publicondemandcost = float(aws_generator.rate * aws_generator.amount)
        
        resource_tags = {}
        
        for key, value in aws_generator.tags.items():
                resource_tags.update({key.replace("resourceTags/user:", ""): value})
        
        self.resourcetags =  resource_tags  
        self.ebs_account_id = int(identity.get("account_number", False))
        self.org_id = int(identity.get("org_id", False))
        self.source = source_uuid
        self.bill_payeraccountid = payer
        self.lineitem_usageaccountid = user
        self.lineitem_usagestartdate = day
        self.month = month
        self.year = year

    def compare_with_panda(self, panda_row: pd.DataFrame) -> bool:
        print(panda_row)
        unfinished_calculations = [
                "lineitem_usageamount",
                "lineitem_unblendedcost",
                "lineitem_blendedcost",
                "pricing_publicondemandcost",
        ]

        for field in self.__dataclass_fields__:
            print(f"Compare {field} *{getattr(self, field)}* with *{panda_row[field]}*")


def read_marketplace_data_to_dataclass(yaml_file_name):

    
    with open(yaml_file_name) as file_obj:
        yaml_file = yaml.safe_load(file_obj)
        accounts = yaml_file.get("accounts", {})
        # Get data for Red Hat Marketplace items
        rh_marketplace_items = []
        
        if "aws" in yaml_file_name.lower():
           
            rh_marketplace_items = [AwsMarketPlaceGenerator(**generator["MarketplaceGenerator"]) for generator in yaml_file["generators"]  if list(generator.keys())[0]=="MarketplaceGenerator" and "Red Hat" in generator["MarketplaceGenerator"].get("legal_entity", [])]
    
    accounts = yaml_file.get("accounts", {})
    return rh_marketplace_items, accounts



df = pd.read_csv('hcs.csv')
print (df)

data, accounts = read_marketplace_data_to_dataclass("aws_static_report_basic.yml")

print(data)


source = "fake_test"
day = "fake_day"
month = "fake_month"
year = "fake_year"

identity = {
            "account_number": "10001",
            "org_id": "1234567",
            "type": "User",
            "user": {"username": "user_dev", "email": "user_dev@foo.com", "is_org_admin": "False", "access": {"aws.account": {"read": ["8888888888885"]},"aws.organizational_unit": {"read": ["QE_OU_002"]}}},
        }

hcs_mock_line_item = [ AwsHcsMockData(source, accounts.get("user")[0], accounts.get("payer") , gen, identity, day, month, year ) for gen in data ]
#print(hcs_mock_line_item)

panda_row = 0

for item in hcs_mock_line_item:
    item.compare_with_panda(df.iloc[panda_row])
    print("*****************++iterate++*********************")
    
    panda_row +=1