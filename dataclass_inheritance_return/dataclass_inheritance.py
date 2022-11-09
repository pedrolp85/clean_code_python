from dataclasses import dataclass
import re

@dataclass
class Animal:
    api_name: str = "animal"
    
    def get_key(self, *args):
        return self.api_name

@dataclass
class Perro(Animal):
    api_name_raza: str = "doberman"
    # We use this key when hitting /azure or ocp_on_azure endpoints
    # we use parent api_name when hittin ocp_on_cloud endpoints
    
    def get_key(self,path):
        if m:=re.search('raza', path):
            return self.api_name_raza
        else:
            return super().get_key()

RAZA_PATH = "/reports/general/"
GENERAL_PATH = "/reports/raza/"

normal_account = Animal()
print(normal_account.get_key(RAZA_PATH))
print(normal_account.get_key(GENERAL_PATH))


azure_account = Perro()
print(azure_account.get_key(RAZA_PATH))
print(azure_account.get_key(GENERAL_PATH))
