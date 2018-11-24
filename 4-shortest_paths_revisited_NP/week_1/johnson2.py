class Graph:

    def __init__(self, file):
        self.file = file
        self.v_total, self.edges, self.graph, self.v_list = self.create_graph()
        self.updated_graph = self.add_vertex()

    def create_graph(file):
        graph = {}
        v_set = set()
        
        with open(file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = [int(s) for s in first_line.split()]
            v_total = graph_details[0]
            e_total = graph_details[1]
            
            for line in adjacency_list:
                l = [int(s) for s in line.split()]
                
                v_set.add(l[1])
                
                graph[(l[1], l[0])] = l[2]
                
            v_list = list(v_set)
        
        return v_total, e_total, graph, v_list


    def add_vertex(v_total, graph):
        update_graph = graph.copy()
        
        for i in range(1, v_total+1):
            update_graph[(v_total+1, i)] = 0
        
        return update_graph

class Node:
    
    def __init__(self, file):
        self.file = file
        self.v_total, self.edges, self.graph, self.v_list = self.create_graph()
        self.updated_graph = self.add_vertex()


def bellman_ford(v_total, v_list, graph):
    dist = {i: float('Inf') for i in v_list}
    dist[v_total] = 0
    weighted_graph = {}
    
    for i in range(v_total-1):
        for u, v in graph:
            if dist[v] > dist[u] + graph[(u, v)]:
                dist[v] = dist[u] + graph[(u, v)]
                
    #negative cycle check
    for edge in graph:
        if dist[edge[0]] + graph[edge] < dist[edge[1]]:
            raise Exception('Graph contains negative weight cycle')
            return
    
    for u, v in graph:
        if u != v_total:
            weighted_graph[(u, v)] = graph[(u,v)] + dist[u] - dist[v]
    
    return weighted_graph, dist



import heapq
def dijkstra(weighted_graph, dist, v_list, source):
    heap_map = {i: float('Inf') for i in v_list}
    parent = {i: None for i in v_list}
    heap_map[source] = 0
    heap_que = [(source, 0)]
    dist_map = {}
    
    while heap_que:
        current = heapq.heappop(heap_que)[0]
        dist_map[current] = heap_map[current]
        
        for edges, d in weighted_graph:
            
        
        for v, d in weighted_graph[current]:
            if v not in dist_map:
                new_distance = heap_map[current] + d
                
                if v in heap_map:
                    if heap_map[v] > new_distance:
                        heap_map[v] = new_distance
                        heapq.heappush(heap_que, (v, new_distance))
                        parent[v] = current
                    
    if dist_map:
        u = min(dist_map)
        v = parent[u]
        min_dist = dist_map[u]
        return min_dist - dist[u] + dist[v]
    
    print(min_dist)
    return


def johnson(file):
    v_total, edges, graph, v_list = create_graph(file)
    update_graph = add_vertex(v_total, graph)
    weighted_graph, dist = bellman_ford(v_total+1, v_list, update_graph)
    
    results = []
    
    for v in v_list:
        solution = (dijkstra(weighted_graph, dist, v_list, v))
        if solution:
            results.append(solution)
    
    return min(results)
    

import time
start_time = time.time()

print(johnson('test_cases/test1.txt'))
#-41

#print(johnson('test_cases/test2.txt'))
#TODO returning -2853
#-3127

#print(johnson('test_cases/test3.txt'))
#negative weight cycle

#print(johnson('test_cases/test4.txt'))
#TODO returning -1173
#-1557


#print(johnson('g1.txt'))
#returning negative weight cycle


#print(johnson('g2.txt'))
#returning negative weight cycle


#print(johnson('g3.txt'))
# returning -5


#print(johnson('large.txt'))
#-6

print("--- %s seconds ---" % (time.time() - start_time))