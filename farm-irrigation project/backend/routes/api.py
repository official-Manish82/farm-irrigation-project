from fastapi import APIRouter, HTTPException
from models.schemas import *
from algorithms.core import *

router = APIRouter()

@router.post("/sort")
def run_sort(req: SortRequest):
    try:
        return merge_sort([field.dict() for field in req.fields])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/kruskal")
def run_kruskal(req: GraphRequest):
    return kruskal_mst(req.matrix)

@router.post("/dijkstra")
def run_dijkstra(req: DijkstraRequest):
    return dijkstra_shortest_path(req.matrix, req.source)

@router.post("/knapsack")
def run_knapsack(req: KnapsackRequest):
    return knapsack_01(req.water_reqs, req.yields, req.capacity)

@router.post("/warshall")
def run_warshall(req: GraphRequest):
    return warshall_closure(req.matrix)

@router.post("/subset-sum")
def run_subset_sum(req: SubsetSumRequest):
    return subset_sum(req.water_reqs, req.target)