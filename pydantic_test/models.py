from pydantic import BaseModel
from typing import List, Optional, Dict
import requests



class Cost(BaseModel):
    value: float
    units: str

class CostReport(BaseModel):
    raw: Cost
    markup: Cost
    usage: Cost
    credit: Cost
    total: Cost

class CostType(BaseModel):
    infrastructure: CostReport
    supplementary: CostReport
    cost: CostReport


class Filter(BaseModel):
    resolution: str
    time_scope_value: int
    time_scope_units: str
    service: Optional[List[str]]
    cluster: Optional[List[str]]
    project: Optional[List[str]]

class Meta(BaseModel):
    count: int
    check_tags: bool
    filter: Filter
    group_by: Dict
    order_by: Dict
    total: CostType


class Links(BaseModel):
    first: Optional[str]
    next: Optional[str]
    previous: Optional[str]
    last: Optional[str]



class APICostReport(BaseModel):
    meta: Meta
    links: Links
    data: List
    


URL = "http://localhost:8000/api/cost-management/v1/reports/"

api_reponse = requests.get(
                f"http://localhost:8000/api/cost-management/v1/reports/gcp/costs/?filter[time_scope_units]=month&filter[time_scope_value]=-1&filter[resolution]=daily&group_by[account]=*"
            )
print(api_reponse.json())

api_pydantic = APICostReport(**api_reponse.json())
print(api_pydantic)