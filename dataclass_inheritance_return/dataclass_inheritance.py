from dataclasses import dataclass
import re

@dataclass
class Account:
    ui_name: str = "Account"
    api_name: str = "account"
    card: str = "Cost by accounts"
    name: str = None
    filter_value: str = None
    
    def get_key(self, *args):
        return self.api_name

@dataclass
class AzureAccount(Account):
    api_name_self_path: str = "subscription_guid"
    # We use this key when hitting /azure or ocp_on_azure endpoints
    # we use parent api_name when hittin ocp_on_cloud endpoints
    
    def get_key(self,path):
        if m:=re.search('openshift', path):
            return self.api_name_self_path
        else:
            return super().get_key()

OCP_ON_GCP_COST_PATH = "/reports/openshift/infrastructures/azure/costs/"
GCP_COST_PATH = "/reports/azure/costs/"

normal_account = Account()
print(normal_account.get_key(OCP_ON_GCP_COST_PATH))
print(normal_account.get_key(GCP_COST_PATH))


azure_account = AzureAccount()
print(azure_account.get_key(OCP_ON_GCP_COST_PATH))
print(azure_account.get_key(GCP_COST_PATH))
