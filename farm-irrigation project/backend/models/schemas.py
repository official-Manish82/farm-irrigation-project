from pydantic import BaseModel
from typing import List, Dict, Any

class FieldData(BaseModel):
    id: int
    water_req: int

class SortRequest(BaseModel):
    fields: List[FieldData]

class GraphRequest(BaseModel):
    matrix: List[List[int]]

class DijkstraRequest(BaseModel):
    matrix: List[List[int]]
    source: int = 0

class KnapsackRequest(BaseModel):
    water_reqs: List[int]
    yields: List[int]
    capacity: int

class SubsetSumRequest(BaseModel):
    water_reqs: List[int]
    target: int