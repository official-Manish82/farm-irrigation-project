import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        result['execution_time_ms'] = round((end - start) * 1000, 4)
        return result
    return wrapper

@measure_time
def explainable_kruskal(matrix):
    n = len(matrix)
    edges = [(matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n) if matrix[i][j] > 0]
    
    steps = [{"text": "Initializing Kruskal's Algorithm. Identifying all possible pipeline connections.", "state": None}]
    
    # Step 1: Sort
    edges.sort()
    steps.append({"text": f"Sorted {len(edges)} potential pipelines by distance/cost (ascending).", "state": None})
    
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        root_i, root_j = find(i), find(j)
        parent[root_i] = root_j

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        steps.append({"text": f"Evaluating pipeline between Field {u} and Field {v} (Cost: {weight}).", "highlight_edge": [u, v]})
        if find(u) != find(v):
            union(u, v)
            mst.append({"from": u, "to": v, "cost": weight})
            total_cost += weight
            steps.append({"text": f"Cycle check passed. Adding pipeline {u}-{v} to the network.", "mst_edge": [u, v]})
        else:
            steps.append({"text": f"Cycle detected! Adding pipeline {u}-{v} would create a loop. Skipping.", "state": None})

    return {
        "total_cost": total_cost,
        "mst_edges": mst,
        "steps": steps,
        "explanation": "Kruskal's Algorithm builds the most cost-effective network by always picking the cheapest available pipeline, provided it doesn't create a closed loop. This ensures every field is connected using the absolute minimum resources.",
        "why_result": f"A total cost of {total_cost} units is the mathematical minimum required to connect all {n} fields.",
        "complexity": "$O(E \\log E)$",
        "analogy": "Imagine building roads between cities. You always build the cheapest, shortest road first, unless those cities are already connected by other roads."
    }

@measure_time
def explainable_dijkstra(matrix, source=0):
    n = len(matrix)
    distances = {i: float('inf') for i in range(n)}
    distances[source] = 0
    visited = set()
    steps = [{"text": f"Starting water flow from the source: Field {source}.", "highlight_node": source}]

    for _ in range(n):
        min_dist = float('inf')
        u = -1
        for i in range(n):
            if i not in visited and distances[i] < min_dist:
                min_dist, u = distances[i], i
        
        if u == -1: break
        visited.add(u)
        steps.append({"text": f"Water reaches Field {u} (Current shortest distance: {distances[u]}).", "highlight_node": u})

        for v in range(n):
            if matrix[u][v] > 0 and v not in visited:
                steps.append({"text": f"Checking path from Field {u} to Field {v} (Pipe length: {matrix[u][v]}).", "highlight_edge": [u, v]})
                if distances[u] + matrix[u][v] < distances[v]:
                    distances[v] = distances[u] + matrix[u][v]
                    steps.append({"text": f"Found a faster route to Field {v}! New shortest distance is {distances[v]}.", "path_update": v})

    safe_distances = {k: (-1 if v == float('inf') else v) for k, v in distances.items()}
    return {
        "distances": safe_distances,
        "source": source,
        "steps": steps,
        "explanation": "Dijkstra's Algorithm systematically explores outward from the water source. It guarantees that the first time it fully 'visits' a field, it has found the absolute shortest route to get there.",
        "why_result": "These distances represent the minimum pressure loss or travel time from the main water pump to every individual field.",
        "complexity": "$O(V^2)$",
        "analogy": "Like pouring water on a tilted network of pipes; the water always naturally flows down the path of least resistance first."
    }

@measure_time
def explainable_knapsack(weights, values, capacity):
    n = len(values)
    steps = [{"text": f"Initializing optimization for {n} fields with a total water budget of {capacity}L.", "state": None}]
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        steps.append({"text": f"Evaluating Field {i-1} (Requires {weights[i-1]}L, Yields ${values[i-1]}).", "highlight_node": i-1})
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    selected = []
    res = dp[n][capacity]
    w = capacity
    for i in range(n, 0, -1):
        if res <= 0: break
        if res == dp[i-1][w]: continue
        selected.append(i-1)
        res -= values[i-1]
        w -= weights[i-1]
        steps.append({"text": f"Selected Field {i-1} for watering to maximize overall farm profit.", "select_node": i-1})

    return {
        "max_yield": dp[n][capacity],
        "selected_fields": selected,
        "steps": steps,
        "explanation": "The 0/1 Knapsack algorithm uses Dynamic Programming. It breaks the complex problem of resource allocation down by making a 'keep or skip' decision for every single drop of water across all combinations of fields.",
        "why_result": f"Watering fields {selected} provides the maximum possible yield (${dp[n][capacity]}) without exceeding the {capacity}L water limit.",
        "complexity": "$O(N \\times W)$",
        "analogy": "Imagine having a backpack with a strict weight limit, and you want to pack the most valuable items inside. You must evaluate the weight-to-value ratio of every combination."
    }

# (Note: For brevity, ensure Sorting, Warshall, and Subset Sum follow this same dictionary return structure with "steps", "explanation", "why_result", etc.)