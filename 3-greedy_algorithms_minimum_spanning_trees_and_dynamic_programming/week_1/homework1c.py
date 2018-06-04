"""
In this programming problem you'll code up Prim's minimum spanning tree algorithm.

Download the text file below.
edges.txt

This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""


def create_graph(file):
    graph = {}
    
    with open(file) as adjacency_list:
        next(adjacency_list)
        for line in adjacency_list:
            single_line = [int(s) for s in line.split()]
            vertex = single_line[0]
            node = single_line[1]
            cost = single_line[2]
            
            if vertex in graph:
                graph[vertex].update({node: cost})
            else:
                graph[vertex] = {node: cost}
    
    return graph



def prim(graph):
    heap_map = {elem:1000000 for elem in range(1, 501)}
    heap_map[1] = 0
    vertex_edge_map = {1: [1,1]}
    edge_cost = {}
    solution = []
    
    while heap_map:
        current = min(heap_map, key=heap_map.get)
#        print(current)
        
        if current in graph:
            for vertex, cost in graph[current].items():
                if vertex not in vertex_edge_map:
                    if cost < heap_map[vertex]:
                        heap_map[vertex] = cost
                        edge_cost[vertex] = cost
                vertex_edge_map[vertex] = [current, vertex]
                            
            solution.append(vertex_edge_map[current])
        heap_map.pop(current)
    
    print('total cost', sum(edge_cost.values()))
    return solution          
    



import heapq

def prim_heapq(graph):
    heap_map = {elem:1000000 for elem in range(0, 501)}
    
    heap_map[1] = 0
    heap_que = [(0, 1)]
    vertex_edge_map = {1: [1,1]}
    edge_cost = {}
    solution = []
    
    
    while heap_que:
        current = heapq.heappop(heap_que)[1]
#        print(current)
        
        if current in graph:
            for vertex, cost in graph[current].items():
                if vertex not in vertex_edge_map:
                    if cost < heap_map[vertex]:
                        heap_map[vertex] = cost
                        heapq.heappush(heap_que, (cost, vertex))
                        edge_cost[vertex] = cost
                        vertex_edge_map[vertex] = [current, vertex]
             
            solution.append(vertex_edge_map[current])
   
    print('total cost', sum(edge_cost.values()))
    return solution  




graph = create_graph('edges.txt')
#prim(graph)
#prim_heapq(graph)


import time
start_time = time.time()
prim(graph)
print("--- %s seconds ---" % (time.time() - start_time))
prim_heapq(graph)
print("--- %s seconds ---" % (time.time() - start_time))