"""
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files describing three graphs:

g1.txt
g2.txt
g3.txt

The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute minu,v∈V d(u,v), where d(u,v) denotes the shortest-path distance from u to v).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

OPTIONAL: Here is a bigger data set to play with.

large.txt

For fun, try computing the shortest shortest path of the graph in the file above.
"""

### BELLMAN FORD ###


def create_graph(file):
    graph = {}
    vertices_list = []
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        graph_details = [int(s) for s in first_line.split()]
        
        for line in adjacency_list:
            l = [int(s) for s in line.split()]
            graph[(l[0], l[1])] = l[2]
            
            if l[0] not in vertices_list:
                vertices_list.append(l[0])
        
    return graph_details[0], graph_details[1], graph, vertices_list


def bellman_ford():
    dist = {vertex: float('Inf') for vertex in vertices_list}
    dist[vertices_list[0]] = 0
#    parent = {vertex: vertex for vertex in vertices_list}
    
    for i in range(vertices-1):
        for u, v in graph:
            if dist[v] > dist[u] + graph[(u, v)]:
                dist[v] = dist[u] + graph[(u, v)]
#                parent[u] = parent[v]
                
    #negative cycle check
    for edge in graph:
        if dist[edge[0]] + graph[edge] < dist[edge[1]]:
            print('Graph contains negative weight cycle')
            return
    
    return min(dist, key=dist.get)
    


import time
start_time = time.time()

#vertices, edges, graph, vertices_list  = create_graph('g1.txt') 
#Graph contains negative weight cycle
#None
#--- 17.121081829071045 seconds ---

#vertices, edges, graph, vertices_list  = create_graph('g2.txt') 
#Graph contains negative weight cycle
#None
#--- 16.92175006866455 seconds ---

vertices, edges, graph, vertices_list  = create_graph('g3.txt') 
#904
#--- 15.45386815071106 seconds ---

#vertices, edges, graph, vertices_list  = create_graph('large.txt') 

print(bellman_ford())
print("--- %s seconds ---" % (time.time() - start_time))