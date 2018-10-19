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

### FLOYD WARSHALL ###

import numpy as np

def create_graph(file):
    graph = {}
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        graph_details = [int(s) for s in first_line.split()]
        
        for line in adjacency_list:
            l = [int(s) for s in line.split()]
            
            if l[0] not in graph:
                graph[l[0]] = {l[1]:l[2]}
            else:
                graph[l[0]].update({l[1]:l[2]})
            
    return graph_details[0], graph_details[1], graph



def initialize_matrix(vertices, edges, graph):
    # create matrix
    #   if no edge, distance is infinity
    #   no self loops. edge is 0. 
    dist_matrix = np.zeros((vertices+1, vertices+1))
#    path = np.zeros((vertices+1, vertices+1))
        
    for i in graph.keys():
        for j in graph[i].keys():
            dist_matrix[i,j] = graph[i][j]
            
    for i in range(1, vertices+1):
        for j in range(1, vertices+1):
            if i != j and dist_matrix[i,j] == 0:
                dist_matrix[i,j] = float('Inf') 
        #         dist_matrix[i,j] = 100000000
    
    return dist_matrix



def floyd_warshall(file):
    vertices, edges, graph  = create_graph(file)
    dist_matrix = initialize_matrix(vertices, edges, graph)
    
    #path = matrix initated at null
    
    for k in range(1, vertices+1):
        for i in range(1, vertices+1):
            for j in range(1, vertices+1):
#                if dist_matrix[i,j] != 0:
                if i != j:
                    dist_matrix[i, j] = min(dist_matrix[i, j],
                       dist_matrix[i, k] + dist_matrix[k, j])

    # test negative cycle
    for i in range(1, vertices+1):
        if dist_matrix[i,i] < 0:
            print('graph contains negative weight cycle')
            return
    
    return dist_matrix.min()


import time
start_time = time.time()

#print(floyd_warshall('test_cases/test1.txt'))
#-41

#print(floyd_warshall('test_cases/test2.txt'))
#-3127
#-3107.0
#--- 8165.598217010498 seconds ---

#print(floyd_warshall('test_cases/test3.txt'))
#negative weight cycle
#graph contains negative weight cycle
#--- 972.4818930625916 seconds ---

#print(floyd_warshall('test_cases/test4.txt'))
#-1557
#-1557
#--- 130.25631713867188 seconds ---


#print(floyd_warshall('g1.txt'))
#


#print(floyd_warshall('g2.txt'))
#


#print(floyd_warshall('g3.txt'))
#TODO returning -16


print(floyd_warshall('large.txt'))
#-6

print("--- %s seconds ---" % (time.time() - start_time))