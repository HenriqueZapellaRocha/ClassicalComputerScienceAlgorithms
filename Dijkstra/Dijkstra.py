import heapq
import math




def addToGraph(graph, initial, finish, weight, vertices):
    if initial not in graph:
        graph[initial] = []
    graph[initial].append((finish,weight))
    
    if initial not in vertices:
        vertices.append(initial)
    if finish not in vertices:
        vertices.append(finish)
        
def dijkstra(graph,start):
    verticesWeight = {}
    
    for vertex in vertices:
        if vertex == start:
            verticesWeight[vertex] = 0
        else:
            verticesWeight[vertex] = math.inf
            
    verticesPQ = []
    heapq.heapify(verticesPQ)
    heapq.heappush(verticesPQ, (verticesWeight[start], start))
    
    while len(verticesPQ) != 0:
        wheight, vertex = heapq.heappop(verticesPQ)

        if vertex in graph:
            for neigboor, edge_wheight in graph[vertex]:
                if verticesWeight.get(neigboor) > edge_wheight + verticesWeight[vertex]:
                    verticesWeight[neigboor] = edge_wheight + verticesWeight[vertex]
                    heapq.heappush(verticesPQ, (verticesWeight[neigboor], neigboor))
                
    return verticesWeight
        
            
        
        
    
graph = {}
vertices = []
with open('/Users/henriquezapellarocha/Documents/pythonStudies/Dijkstra/grafo.txt', 'r') as archive:
    for line in archive:
        originVertex, rest = line.split(" -> ")
        finalVertex, edgeWeight = rest.strip().split(": ")
        addToGraph(graph,int(originVertex),int(finalVertex),int(edgeWeight),vertices)





print(dijkstra(graph,1))