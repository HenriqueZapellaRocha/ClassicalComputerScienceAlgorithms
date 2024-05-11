import heapq
import math
from operator import ne

graph = {}

def addToGraph(graph, startVertex, finalVertex, weight,vertices):
    if startVertex not in graph:
        graph[startVertex] = []
        vertices.append(startVertex)
    if finalVertex not in graph: 
        graph[finalVertex] = []
        vertices.append(finalVertex)
    
    graph[startVertex].append((finalVertex, weight))
    graph[finalVertex].append((startVertex, weight))
    
def prim(graph,start,vertices):
    key = {}
    dead = {}
    verticesPQ = []
    visited = []
    
    for vertex in vertices:
        key[vertex] = math.inf
        dead[vertex] = None
    key[start] = 0
    
    heapq.heapify(verticesPQ)
    heapq.heappush(verticesPQ, (0,start))

    while len(verticesPQ) != 0:
        actual_key, vertex = heapq.heappop(verticesPQ)
        visited.append(vertex)
        for neighboor, wheight in graph[vertex]:
            if neighboor not in visited and wheight < key[neighboor]:
                dead[neighboor] = vertex
                key[neighboor] = wheight
                heapq.heappush(verticesPQ,(wheight, neighboor))

    return toNewGraph(key,dead)

def toNewGraph(key,dead):
    newGraph = {}
    
    for actualDead in dead:
        if dead.get(actualDead) != None:
            if actualDead not in newGraph:
                newGraph[actualDead] = []
            newGraph[actualDead].append((dead.get(actualDead),key[actualDead]))
            if dead.get(actualDead) not in newGraph:
                newGraph[dead.get(actualDead)] = []
            newGraph[dead.get(actualDead)].append((actualDead, key[actualDead]))
        
    return newGraph
    
graph = {}
vertices = []
with open('Dijkstra/grafo.txt', 'r') as archive:
    for line in archive:
        originVertex, rest = line.split(" -> ")
        finalVertex, edgeWeight = rest.strip().split(" : ")
        addToGraph(graph,originVertex,finalVertex,int(edgeWeight),vertices)
        addToGraph(graph,finalVertex,originVertex,int(edgeWeight),vertices)
print((graph))
print()
print(prim(graph,"A",vertices))