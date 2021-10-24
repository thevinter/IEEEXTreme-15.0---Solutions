from collections import defaultdict
    
def dij(nodes, distances, current, removed):
    unvisited = {node: None for node in nodes if node != removed} #using None as +inf
    previous = {node: None for node in nodes if node != removed}
    visited = {}
    currentDistance = 0
    unvisited[current] = currentDistance
    
    while True:
        if current in distances:
            for neighbour, distance in distances[current].items():
                if neighbour not in unvisited or neighbour == removed:
                    continue
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
                    previous[neighbour] = current
            visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        # print(candidates)
        # print(unvisited)
        if len(candidates) == 0:
            break
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    
    return visited, previous
    

[N,M,S,T] = input().split(" ")
N = int(N)
M = int(M)
S = int(S)
T = int(T)

nodes = [n+1 for n in range(N)]
arcs = {}
    
for m in range(M):
    [a,b,d] = input().split(" ")
    a = int(a)
    b = int(b)
    d = int(d)
    if not a in arcs:
        arcs[a] = {}
    if not b in arcs:
        arcs[b] = {}
    arcs[a][b] = d
    arcs[b][a] = d
    
    
# print("Original:")
distances, previous = dij(nodes, arcs, S, None)
# print(distances)
# print(previous)

maxDist = -1
maxNode = -1

removed = previous[T]
while removed != S:
    # print(f"Removed {removed}:")
    distances2, previous2 = dij(nodes, arcs, S, removed)
    
    if previous2[T] != None:
        if distances2[T] > maxDist:
            maxDist = distances2[T]
            maxNode = removed
    
    
    # print(distances2)
    # print(previous2)
    removed = previous[removed]

print(maxNode)
