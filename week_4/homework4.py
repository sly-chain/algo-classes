"""
The file contains the adjacency list representation of a simple undirected graph. 
There are 200 vertices labeled 1 to 200. The first column in the file represents 
the vertex label, and the particular row (other entries except the first column) 
tells all the vertices that the vertex is adjacent to. So for example, the 6th 
row looks like : "6 155 56 52 120 ......". This just means that the vertex with 
label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the 
min cut problem and use it on the above graph to compute the min cut. (HINT: 
Note that you'll have to figure out an implementation of edge contractions. 
Initially, you might want to do this naively, creating a new graph from the 
old every time there's an edge contraction. But you should also think about 
more efficient implementations.) (WARNING: As per the video lectures, please 
make sure to run the algorithm many times with different random seeds, and 
remember the smallest cut that you ever find.) Write your numeric answer in 
the space provided. So e.g., if your answer is 5, just type 5 in the space 
provided.
"""

import random

class Graph(object):
    def __init__(self, file):
        self._file = file


    def _create_graph(self):
        graph = {}
        
        with open(self._file) as adjacency_list:
            for line in adjacency_list:
                single_line = [int(s) for s in line.split()]
                graph[single_line[0]] = single_line[1:]
                
        return graph

graph = Graph._create_graph('week_4/kargerMinCut.txt')

# choose random edge 
def get_random_edge():
    """
    pick random key
    then pick random value from that key
    """
    v1 = random.choice(list(graph))
    v2 = random.choice(v1)
    
    return v1, v2
        
# contract chosen edge
def contract():
    v1, v2 = get_random_edge()

  # add vertices from graph[v2] to graph[v1]
  # delete graph[v2]
    graph[v1].extend[graph(v2)]
    del graph[v2]
    
  # delete any references to v2  
    for k, v in graph.iteritems():
        graph[k].remove(v2)
  
  # remove self loops
    for v in graph[v1]:
        if v == v1:
            graph[v1].remove(v1)
    

def min_cut():
    while len(graph) <2:
        contract()
    # count the edges
    

# repeat algorithm N times
        

