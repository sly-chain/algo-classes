"""
In this question your task is again to run the clustering algorithm from 
lecture, but on a MUCH bigger graph. So big, in fact, that the distances 
(i.e., edge costs) are only defined implicitly, rather than being provided 
as an explicit list.


The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file 
"0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" 
denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the 
Hamming distance--- the number of differing bits --- between the two nodes' 
labels. For example, the Hamming distance between the 24-bit label of node #2 
above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 
(since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a 
k-clustering with spacing at least 3? That is, how many clusters are needed to 
ensure that no pair of nodes with all but 2 bits in common get split into 
different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably 
can't write it out explicitly, let alone sort the edges by cost. So you will 
have to be a little creative to complete this part of the question. 
For example, is there some way you can identify the smallest distances without 
explicitly looking at every pair of nodes?
"""

import time
import itertools
import random


class Graph:

    def __init__(self, file):
        self.file = file
        self.clusters = {}
        self.rank = {}
        self.graph_details, self.graph = self.create_graph()
        self.parent = {}
    
    
    def create_graph(self):
        graph = {}
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = [int(s) for s in first_line.split()]
            i = 1
    
            for line in adjacency_list:
                single_line = [int(s) for s in line.split()]
                
                if single_line not in graph.values():
                    graph[i] = single_line
                i+=1
    
        return graph_details, graph
    
    
    def find_parent(self, v):
        if self.parent[v] == v:
            return self.parent[v]
        return self.find_parent(self.parent[v])
    
    
    def update_parent(self, v, n):
        v_root = self.find_parent(v)
        n_root = self.find_parent(n)
        
        if self.rank[n_root] < self.rank[v_root]:
            self.parent[n_root] = v_root
            
        elif self.rank[v_root] < self.rank[n_root]:
            self.parent[v_root] = n_root
            
        else:
            self.parent[n_root] = v_root
            self.rank[v_root] += 1
    
    
    
    def kruskal(self):
        i = 0
        result = []
        
        for subset in self.graph:
            parent_1 = self.find_parent(subset[1])
            parent_2 = self.find_parent(subset[2])
            
            if parent_1 != parent_2:
                result.append(subset[0])
                i += 1
                self.update_parent(subset[1], subset[2])
                
        return sum(result)
    
    
    def bit_array(self, current, num):
        n_spaces = []
        combos = list(itertools.permutations(range(len(current)), num))
        
        for c in combos:
            test = current[:]
            for n in range(num):
                test[c[n]] ^= 1
                
            n_spaces.append(test)
        
        return n_spaces
    
    
    def k_cluster(self):
        self.rank = {elem:0 for elem in range(1, self.graph_details[0] + 1)}
        self.parent = {elem:elem for elem in range(1, self.graph_details[0] + 1)}
        
        node_list = self.graph.copy()
        nodes_length = len(self.graph)
        
        bit_flip_array = []
        
        while node_list:
            nodes = node_list.copy()
            nodes_keys = list(nodes.keys())
            nodes = node_list.copy()
            
            current = nodes_keys[0]
            bits = node_list.pop(current)
            
            parent1 = self.find_parent(current)
            
            
            for k, v in nodes.items():
                parent2 = self.find_parent(k)
                
                if parent1 != parent2:
                    bit_flip_array = []
                    one_space = self.bit_array(bits, 1)
                    bit_flip_array.extend(one_space)
#                    two_space = self.bit_array(bits, 2)
#                    bit_flip_array.extend(two_space)
                    
                    if v in bit_flip_array:
                        self.update_parent(current, k)
#                        node_list.pop(k)
                        nodes_length -= 1
            
        return nodes_length
                    
            



start_time = time.time()
g = Graph('test_cases/test1.txt')
#3946

#g = Graph('test_cases/test2.txt')
#127

#g = Graph('test_cases/test3.txt')
#15

#g = Graph('test_cases/test3.txt')
#1371

#g = Graph('clustering_big.txt')
#6119

print('end', g.k_cluster())
print("--- %s seconds ---" % (time.time() - start_time))

