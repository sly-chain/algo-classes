"""
In this programming problem and the next you'll code up the clustering algorithm 
from lecture for computing a max-spacing k-clustering.

Download the text file below.
clustering1.txt

This file describes a distance function (equivalently, a complete graph with 
edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j) for each choice of 1 ≤ i < j ≤ n, where n is the 
number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the 
distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 
5250. You can assume that distances are positive, but you should NOT assume 
that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on 
this data set, where the target number k of clusters is set to 4. What is the 
maximum spacing of a 4-clustering?

"""


import numpy as np
import itertools
import time

class Graph:

    def __init__(self, file, k):
        self.file = file
        self.k = k
        self.clusters = {}
        self.rank = {}
        self.graph_details, self.graph = self.create_graph()


    def create_graph(self):
        edges_graph = []
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = int(first_line)
    
            for line in adjacency_list:
                single_line = [int(s) for s in line.split()]
                vertex = single_line[0]
                node = single_line[1]
                cost = single_line[2]
                
                edges_graph.append([(vertex, node), cost])
        
        return graph_details, sorted(edges_graph, key=lambda x: x[1])
    
    
    def find_centroid(self, n):
        for centroid, node in self.clusters.items():   
            if n in node:
                return centroid
    
    
    def find_distance(self, e):
        for subset in self.graph:
            if (e[0], e[1]) in subset:
                return subset[1]
    
    
    def distance_matrix(self):
        distances = []
        matrix = np.array(list(itertools.permutations(self.clusters.keys(), 2)))
        
        for i in matrix:
            distances.append(self.find_distance(i))
        
        return max(x for x in distances if x is not None)
    

    def k_means(self):
        self.clusters = {elem:[elem] for elem in range(1, self.graph_details+1)}
        i=0
        
        for subset in self.graph:
            
            centroid_1 = self.find_centroid(subset[0][0])
            centroid_2 = self.find_centroid(subset[0][1])
            
            if len(self.clusters) == self.k:
                break
            
            if centroid_1 != centroid_2:
                self.clusters[centroid_1].extend(self.clusters[centroid_2])
                del self.clusters[centroid_2]
                i += 1
                
        return self.distance_matrix()
            
        
g = Graph('clustering1.txt', 4) 
start_time = time.time()
print(g.k_means())
print("--- %s seconds ---" % (time.time() - start_time))
# 7503

