from __future__ import annotations

import csv
from dataclasses import dataclass



def read_csv_helper(filepath):
  content = []
  with open(filepath) as csvfile:
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)

    for row in csv_reader:
      row_data = {key: value for key, value in zip(headers, row)}
      content.append(row_data)

  return content

@dataclass
class LoadBalancing():
    file_header: str = "load balancing"


class AWSLoadBalancing(LoadBalancing):
    name: str = "ELB"

class AzureLoadBalancing(LoadBalancing):
    name: str = "Load Balancer"

    "load balancing": "Load Balancer",
    "Object_storage": "Blob Storage",
    "dns": "Azure DNS" ,

@dataclass
class AWSExpectedLineFile():
    load_balancer: AWSLoadBalancing
