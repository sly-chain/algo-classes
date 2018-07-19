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

class Node:
    def __init__(self, index, label):
        self.index = index
        self.label = label
#        self.rank = None
#        self.parent = None


class Graph:
    def __init__(self, file):
        self.file = file
        self.graph_details, self.graph = self.create_graph()
        self.nodes_length = len(self.graph)
#        self.rank = []
    
    
    def create_graph(self):
        graph = []
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = [int(s) for s in first_line.split()]
            seen = set()
            i = 1
    
            for line in adjacency_list:
                single_line = str(line.strip().replace(' ', ''))
                node = Node(i, single_line)
                
                if node.label not in seen:
                    graph.append(node)
                
                seen.add(node.label)
                i+=1
        
        return graph_details, graph
    
    
    def hamming_dist(self, a, b):
        return sum(ch1 != ch2 for ch1, ch2 in zip(a, b))
    
    
    def k_cluster(self):
        print(len(self.graph))
        node_list = self.graph.copy()
#        self.parent = [elem for elem in range(self.graph_details[0])]
#        self.rank = [0 for elem in range(self.graph_details[0])]
        
        while node_list:
            nodes = node_list.copy()
            current = node_list.pop(0)

            for n in nodes:
                if self.hamming_dist(current.label, n.label) in [1, 2]:
                    node_list.remove(n)
#                        node_list.remove(current)
                    self.nodes_length -= 1
            
        return self.nodes_length
                    


start_time = time.time()
#g = Graph('test_cases/test1.txt')
#4096 -- 3946
#end 3950
#--- 32.82023501396179 seconds ---

#g = Graph('test_cases/test2.txt')
#128 -- 127

#g = Graph('test_cases/test3.txt')
#16 -- 15

#g = Graph('test_cases/test4.txt')
#65536 -- 1371
#end 25062
#--- 2805.9299211502075 seconds ---

g = Graph('test_cases/test5.txt')
#16384 -- 8714
#end 11238
#--- 326.2632009983063 seconds ---

#g = Graph('clustering_big.txt')
#200000 -- 6119

print('end', g.k_cluster())
print("--- %s seconds ---" % (time.time() - start_time))

