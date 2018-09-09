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


def create_graph(file):
    graph = []
    
    with open(file) as adjacency_list:
#            
        for line in adjacency_list:
            graph.append([int(s) for s in line.split()])
        
    return graph[0], graph[1:]


graph_details, graph = create_graph('g1.txt')



def bellman_ford():
    
    
    
    pass









import time
start_time = time.time()

#graph_details, graph = create_graph('g1.txt') 

#graph_details, graph = create_graph('g2.txt') 

#graph_details, graph = create_graph('g3.txt') 

#graph_details, graph = create_graph('large.txt') 


print('end', bellman_ford())


print("--- %s seconds ---" % (time.time() - start_time))