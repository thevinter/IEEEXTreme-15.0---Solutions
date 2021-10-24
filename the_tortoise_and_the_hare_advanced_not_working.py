from collections import defaultdict
import heapq
import random
from functools import cmp_to_key

def dij(nodes, distances, current, removed):
    unvisited = {node: None for node in nodes if node != removed} #using None as +inf
    previous = {node: None for node in nodes if node != removed}
    nexts = {node: [] for node in nodes if node != removed}

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
                    nexts[current].append(neighbour)
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
        

    return visited, previous, nexts
    
def hasArc(arcs, fr, to):
    return (fr in arcs) and (to in arcs[fr])

def cmpWNone(a,b):
    if a == None:
        if b == None:
            return 0
        else:
            return 1
    else:
        if b == None:
            return -1
        else:
            return -1 if a<b else (1 if a>b else 0);
    

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
    


distances, previous, nexts = dij(nodes, arcs, S, None)
print("Dist:", distances)
print("Prev:", previous)
print("Next:", nexts)



SPTvi  = [T]
vi = previous[T]
while vi != S:
    SPTvi.insert(0, vi)
    vi = previous[vi]
SPTvi.insert(0, S)
print("SPTvi:", SPTvi)


# insert every Oi node into a heap Hi
heaps = []
dists = [distances]

origDists = distances.copy()
K = len(SPTvi) - 1; # K = 4 for the first example
for i in range(1,K):
    vi = SPTvi[i];
    print(f"vi[i={i}]: {vi}")
    heapdict = {}
    distances = origDists.copy()
    
    Ui = []
    tovisit = [S]
    while len(tovisit) > 0:
        nexttovisit = []
        for node in tovisit:
            if node == vi:
                continue
            Ui.append(node)
            nexttovisit += nexts[node]
        tovisit = nexttovisit
    print(f" - Ui[i={i}]: {Ui}")
    
    
    tovisit = [nxt for nxt in nexts[vi] if nxt != SPTvi[i+1]]
    while len(tovisit) > 0:
        nexttovisit = []
        for node in tovisit:
            if node == SPTvi[i+1]:
                continue
            
            # find the min distance between x and u
            minDist = None
            for u in Ui:
                if not hasArc(arcs, node, u):
                    continue
                
                dist = distances[u] + arcs[node][u] if distances[u] != None else None
                if dist == None:
                    continue
                if minDist == None or dist < minDist:
                    minDist = dist
            
            heapdict[node] = minDist
            nexttovisit += nexts[node]
        tovisit = nexttovisit
    print(f" - Hi[i={i}]: {heapdict}")
    
    if vi == 4:
        print("test")
    
    while len(heapdict) > 0:
        node, dist = sorted(heapdict.items(), key=cmp_to_key(cmpWNone))[0]
        distances[node] = dist
        del heapdict[node]
        print(heapdict);
        
        for node2 in heapdict:
            if not hasArc(arcs, node, node2):
                continue
            
            dist2 = distances[node] + arcs[node][node2] if distances[node] != None else None;
            if dist2 == None:
                continue
            if heapdict[node2] == None or dist2 < heapdict[node2]:
                heapdict[node2] = dist2
    heaps.append(heapdict)
    dists.append(distances.copy())
    print(f" - distances: {distances}")
print(f"dists:")
print("\n".join([str(d) for d in dists]))


    

# for removed in toremove:
    # del heapdi
