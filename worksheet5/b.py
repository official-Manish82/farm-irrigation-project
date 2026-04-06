def warshall(graph):
    n = len(graph)
    
   
    reach = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    return reach

graph = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

result = warshall(graph)

print("Transitive Closure:")
for row in result:
    print(row)