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

### JOHNSON ###


def create_graph(file):
    graph = {}
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        graph_details = [int(s) for s in first_line.split()]
        
        for line in adjacency_list:
            l = [int(s) for s in line.split()]
            graph[(l[0], l[1])] = l[2]
    print("create--- %s seconds ---" % (time.time() - start_time))
    return graph_details[0], graph_details[1], graph


def add_vertex(vertices, graph):
    update_graph = graph.copy()
    
    for i in range(1, vertices+1):
        update_graph[(vertices+1, i)] = 0
    print("update--- %s seconds ---" % (time.time() - start_time))
    return update_graph


def bellman_ford(vertices, graph):
    dist = {i: float('Inf') for i in range(1, vertices+1)}
    dist[vertices] = 0
    weighted_graph = {}
    
    for i in range(vertices-1):
        for u, v in graph:
            if dist[v] > dist[u] + graph[(u, v)]:
                dist[v] = dist[u] + graph[(u, v)]
                
    #negative cycle check
    for edge in graph:
        if dist[edge[0]] + graph[edge] < dist[edge[1]]:
            raise Exception('Graph contains negative weight cycle')
            return
    
    for u,v in graph:
        if u != vertices:
            if u in weighted_graph:
                weighted_graph[u].append((v, graph[(u,v)] + dist[u] - dist[v]))
            else:
                weighted_graph[u] = [(v, graph[(u,v)] + dist[u] - dist[v])]
    u = min(dist, key=dist.get)
    print(dist[u])
    print("bellman--- %s seconds ---" % (time.time() - start_time))
    return weighted_graph, dist


import heapq
# https://github.com/DanielStutzbach/heapdict/blob/master/heapdict.py
# TODO try with heapdict one of these days

def dijkstra(graph, weighted_graph, dist, vertices, source):
    heap_map = {i: float('Inf') for i in range(1, vertices+1)}
    parent = {i: None for i in range(1, vertices+1)}
    heap_map[source] = 0
    heap_que = [(0, source)]
    dist_map = {}
    
    while heap_que:
        current = heapq.heappop(heap_que)[1]
#        print(current)
        if current in weighted_graph:
            for v, d in weighted_graph[current]:
                if v not in dist_map:
                    new_distance = heap_map[current] + d
                    if heap_map[v] > new_distance:
                        heap_map[v] = new_distance
                        heapq.heappush(heap_que, (new_distance, v))
                        parent[current] = v
                    
            dist_map[current] = heap_map[current]

    if dist_map:
        u = min(dist_map, key=dist_map.get)
        v = parent[u]
        if v:
            min_dist = dist_map[u]
            return min_dist - dist[u] + dist[v]
    
    return


def johnson(file):
    #create modified graph with new source vertex
    #use bellman ford to find shortest path from source to every vertex in graph
    #update edge lengths
    #run dykstra
    #return shortest shortest path
    
    vertices, edges, graph = create_graph(file)
#    print(graph)
    update_graph = add_vertex(vertices, graph)
    weighted_graph, dist = bellman_ford(vertices+1, update_graph)
    results = []
    
    for v in range(1, vertices):
        solution = (dijkstra(graph, weighted_graph, dist, vertices, v))
        if solution:
            results.append(solution)
    
    return min(results)
    

import time
start_time = time.time()

#print(johnson('test_cases/test1.txt'))
#-41
#min(dist) = -41
#--- 0.0012319087982177734 seconds ---

#print(johnson('test_cases/test3.txt'))
#negative weight cycle


#print(johnson('test_cases/test2.txt'))
#TODO returning -2853
#min(dist) = -3118
#--- 70.03622913360596 seconds ---
#-3127


#print(johnson('test_cases/test4.txt'))
#TODO returning -1351
#min(dist) = -1467
#--- 1.7071361541748047 seconds ---
#-1467


#print(johnson('g1.txt'))
#returning negative weight cycle


#print(johnson('g2.txt'))
#returning negative weight cycle


#print(johnson('g3.txt'))
#returning -17
#min(dist) = -19
#--- 42.68953490257263 seconds ---

print(johnson('large.txt'))
#TODO 
#min(dist) = -6
#bellman--- 33081.50987124443 seconds ---
#-6

print("--- %s seconds ---" % (time.time() - start_time))