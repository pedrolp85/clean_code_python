import itertools
import pytest


single_element = "single_item"

double_element = ["first_element", "second_element", "third_element"]

triple_element = ["one", "two", "three", "four"]


zip_iterable = zip(itertools.repeat(single_element), *zip(*itertools.product(double_element[1:], triple_element[1:])))


for item in zip_iterable:
    print(item)


all_query_param = [
    pytest.param(None, id="query-none"),
    pytest.param(
        {"resolution": "daily", "time_scope_value": -10, "time_scope_units": "day"},
        id="last-10-days",
    ),
    pytest.param(
        {"resolution": "daily", "time_scope_value": -30, "time_scope_units": "day"},
        id="last-30-days",
    ),
    """
    pytest.param(
        {"resolution": "daily", "time_scope_value": -90, "time_scope_units": "day"},
        id="last-90-days",
    ),
    pytest.param(
        {"resolution": "daily", "time_scope_value": -1, "time_scope_units": "month"},
        id="last-month-daily",
    ),
    pytest.param(
        {"resolution": "daily", "time_scope_value": -2, "time_scope_units": "month"},
        id="two-months-ago-daily",
    ),
    pytest.param(
        {"resolution": "monthly", "time_scope_value": -1, "time_scope_units": "month"},
        id="last-month",
    ),
    pytest.param(
        {"resolution": "monthly", "time_scope_value": -2, "time_scope_units": "month"},
        id="two-months-ago",
    ),
    """
    
]

aws_group_by_param = [
    pytest.param(None, id="group-by-none"),
    pytest.param({"account": "*"}, id="account"),
    pytest.param({"region": "*"}, id="region"),
    #pytest.param({"service": "*"}, id="service"),
    #pytest.param({"instance_type": "*"}, id="instance_type"),
    #pytest.param({"aws_category:name": "*"}, id="awscategory_name"),
    #pytest.param({"aws_category:cost_env": "*"}, id="awscategory_env"),
    #pytest.param({"aws_category:qe_source": "*"}, id="awscategory_source"),
]

AWS_COST_PATH = "/api/cost/aws"

"""
def get_function_parameters():
    for endpoint,group_by,report_filter in zip(itertools.repeat(aws_group_by_param[1]) , *zip(*itertools.product(aws_group_by_param[1:], all_query_param[1:]))):
        yield endpoint,group_by,report_filter

@pytest.mark.parametrize("endpoint,group_by,report_filter", 
                         
                            zip(itertools.repeat(aws_group_by_param[1].values) , *zip(*itertools.product(aws_group_by_param[1:], all_query_param[1:]))),
                        
                         )
                        #zip(itertools.repeat(aws_group_by_param[1]) , *zip(*itertools.product(aws_group_by_param[1:], all_query_param[1:]))),
@pytest.mark.parametrize("list_quantity", [2, 4, 8])
def test_api(
    group_by,
    list_quantity,
    endpoint,
    report_filter,
):


    print(f"endopoint {endpoint}")
    #print(f"report_filter {report_filter.values}")

    pass
"""

@pytest.mark.parametrize("endpoint,group_by,report_filter", 
                         [
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "daily", "time_scope_value": -10, "time_scope_units": "day"},id="cost-account-last10days"),
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "daily", "time_scope_value": -30, "time_scope_units": "day"},id="cost-account-last30days"),
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "daily", "time_scope_value": -90, "time_scope_units": "day"},id="cost-account-last90days"),
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "daily", "time_scope_value": -1, "time_scope_units": "month"},id="cost-account-last-month-daily"),         
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "daily", "time_scope_value": -2, "time_scope_units": "month"},id="cost-account-two-months-ago-daily"),         
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "monthly", "time_scope_value": -1, "time_scope_units": "month"},id="cost-account-last-month-monthly"),                            
                            pytest.param(AWS_COST_PATH,{"account": "*"},{"resolution": "monthly", "time_scope_value": -2, "time_scope_units": "month"},id="cost-account-two-months-ago-monthly"),
                        
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "daily", "time_scope_value": -10, "time_scope_units": "day"},id="cost-account-last10days"),
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "daily", "time_scope_value": -30, "time_scope_units": "day"},id="cost-account-last30days"),
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "daily", "time_scope_value": -90, "time_scope_units": "day"},id="cost-account-last90days"),
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "daily", "time_scope_value": -1, "time_scope_units": "month"},id="cost-account-last-month-daily"),         
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "daily", "time_scope_value": -2, "time_scope_units": "month"},id="cost-account-two-months-ago-daily"),         
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "monthly", "time_scope_value": -1, "time_scope_units": "month"},id="cost-account-last-month-monthly"),                            
                            pytest.param(AWS_COST_PATH,{"service": "*"},{"resolution": "monthly", "time_scope_value": -2, "time_scope_units": "month"},id="cost-account-two-months-ago-monthly"),
                            
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "daily", "time_scope_value": -10, "time_scope_units": "day"},id="cost-account-last10days"),
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "daily", "time_scope_value": -30, "time_scope_units": "day"},id="cost-account-last30days"),
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "daily", "time_scope_value": -90, "time_scope_units": "day"},id="cost-account-last90days"),
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "daily", "time_scope_value": -1, "time_scope_units": "month"},id="cost-account-last-month-daily"),         
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "daily", "time_scope_value": -2, "time_scope_units": "month"},id="cost-account-two-months-ago-daily"),         
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "monthly", "time_scope_value": -1, "time_scope_units": "month"},id="cost-account-last-month-monthly"),                            
                            pytest.param(AWS_COST_PATH,{"region": "*"},{"resolution": "monthly", "time_scope_value": -2, "time_scope_units": "month"},id="cost-account-two-months-ago-monthly"),

                         ]
                         )
                        #zip(itertools.repeat(aws_group_by_param[1]) , *zip(*itertools.product(aws_group_by_param[1:], all_query_param[1:]))),
@pytest.mark.parametrize("list_quantity", [2, 4, 8])
def test_api_explicit_params(
    group_by,
    list_quantity,
    endpoint,
    report_filter,
):


    print(f"endopoint {endpoint}")
    print(f"group_by {group_by}")
    print(f" report_filter {report_filter}")
    #print(f"report_filter {report_filter.values}")

    pass