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


def create_graph(file):
    graph = {}
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        graph_details = [int(s) for s in first_line.split()]
        i = 1

        for line in adjacency_list:
            single_line = [int(s) for s in line.split()]
            
            if single_line not in graph.values():
                graph[i] = single_line
            i+=1
            
    return graph_details, graph


#def flip_bit(number, n):
#    return (number // 10**n % 10)^1



#def distance_one(current):
#    one_space = []
#    i = 1
#    for i in range(len(current)):
#        test = current[:]
#        test[i]^=1
#        print(test)
#        one_space.append(test)
#        i += 1
#    
#    return one_space
        

def bit_array(current, num):
    n_spaces = []
    combos = list(itertools.permutations(range(len(current)), num))
    
    for c in combos:
        test = current[:]
        for n in range(num):
            test[c[n]] ^= 1
            
        n_spaces.append(test)
    
    return n_spaces


def k_cluster():
    node_list = graph.copy()
    nodes_length = len(graph)
    k_array = []
    
    while node_list:
        nodes = node_list.copy()
        node_keys = list(nodes.keys())
#        print(len(node_list))
        current = node_list.pop(node_keys[0])
        bit_flip_array = []
        
        one_space = bit_array(current, 1)
        two_space = bit_array(current, 2)
        bit_flip_array.extend(one_space)
        bit_flip_array.extend(two_space)
        
        for k, v in node_list.items():
            if v in bit_flip_array:
                nodes.pop(k)
                k_array.append(k)
                nodes_length -= 1
    
    return nodes_length, len(nodes)  




start_time = time.time()

#graph_details, graph = create_graph('test_cases/test1.txt')
#4096 -- 3946
#end (3946, 1)
#--- 169.542249917984 seconds ---

#graph_details, graph = create_graph('test_cases/test2.txt')
#128 -- 127

#graph_details, graph = create_graph('test_cases/test3.txt')
#16 -- 15

graph_details, graph = create_graph('test_cases/test4.txt')
#65536 -- 1371

#graph_details, graph = create_graph('test_cases/test5.txt')
#16384 -- 8714
#end (8270, 1)
#--- 2368.702915906906 seconds ---


#graph_details, graph = create_graph('clustering_big.txt')  
#200000 -- 6119

print('end', k_cluster())
print("--- %s seconds ---" % (time.time() - start_time))





#end 198788
#--- 1443.6360261440277 seconds ---

