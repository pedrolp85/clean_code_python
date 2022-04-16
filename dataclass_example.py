from dataclasses import dataclass

import pytest

@dataclass
class GCP_details:
    pass 

@dataclass
class Account(GCP_details):
    ui_name : str =  'Account'
    api_name : str =  'account'
    card : str =  'Cost by accounts'
    name : str = None

@dataclass
class Service(GCP_details):
    ui_name : str = 'Service'
    api_name : str = 'service'
    card : str = 'Cost by services'
    name: str = None

@dataclass
class Region(GCP_details):
    ui_name : str = 'Region'
    api_name: str = 'region'
    card: str = 'Cost by regions'
    name: str = None

if __name__ == "__main__" :

    account = Account(account_name = "nombre de cuenta")
    service = Service(service_name = "nombre de servicio")
    region = Region()

    '''

    print(account)
    print(service)
    print(region)

    service.service_name = "Cloud DNS"
    region.region_name = "us_west"

    print(service)
    print(region)

    for i in account, service, region:
        print (i.card_name)
        print(i.ui_name)
        
        if i == service:
            print("Esto es un servicio")
            print(i)
        else:
            print(i)
    '''

@pytest.mark.parametrize("group_by", [Account(), Service(), Region()])
#@pytest.mark.parametrize("group_by", ["account", "service", "region"])
def test_ui_gcp_details_cost_items_match_api(group_by):
    """Verify that the data in cost item details rows matches api

    metadata:
        requirements: cost_gcp_details
    """

    iterate_list = [ i for i in (Account(), Service(), Region()) if i != group_by ]

    max_items = [ "value1", "value2", "value3" ]

    for i in range(len(max_items)):
        group_by.name = max_items[i]
        #button = view.all_items[i]
        #button.click()
        print(group_by)

        for element in iterate_list:
            
            card = element.card
            
            report_filter = f"{group_by.api_name}: {group_by.name}"
            
            print("card,",  element.card)
            print(element.ui_name)
            print(element.api_name)
            '''
            gcp_cost_report = call_api(
                PATH, application, filter=report_filter, group_by={card_api_name: "*"}
            )

            line_items = report_line_items(gcp_cost_report["data"])
            api_items = [
                (item[card_api_name], round_api_value(item["cost"]["total"]["value"]))
                for item in line_items
            ]

            view.cost_item_details.select_card(card)
            '''


            '''
            assert len(api_items) == len(ui_items), "both api and ui have the same n of elements"
            for i in ui_items:
                assert i in ui_items, "for each api item, assert it is displayed on UI"

        view.cost_item_details.back_breadcrumb.click()
        assert view.is_displayed
            '''