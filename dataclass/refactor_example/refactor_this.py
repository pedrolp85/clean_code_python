import pytest
from helpers import read_csv_helper
from helpers import AWSExpectedLineFile()
from helpers import AzureModel


AZURE_MODEL = {
    "load balancing": "Load Balancer",
    "Object_storage": "Blob Storage",
    "dns": "Azure DNS" ,
}

AWS_MODEL = {
    "load balancing": "ELB",
    "Object_storage": "S3 Buckets",
    "dns": "Route53" ,
}

@pytest.mark.parametrize("cloud", ["amazon", "azure"])
def test_amazon_csv_content(cloud):

    if cloud == "Amazon":
        path = "amazon_file.csv"
        model = AWS_MODEL
    else:
        path = "azure_file.csv"
        model = AZURE_MODEL

    content = read_csv_helper(path)

    for line in content:
        for key in line.keys():
            assert line[key] == model[key]
