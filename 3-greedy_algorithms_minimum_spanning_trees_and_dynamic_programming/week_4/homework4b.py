"""
This problem also asks you to solve a knapsack instance, but a much bigger one.

Download the text file below.
knapsack_big.txt

This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.

This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

import numpy as np


def create_graph(file):
    graph = []
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        graph_details = [int(s) for s in first_line.split()]
            
        for line in adjacency_list:
            single_line = [int(s) for s in line.split()]
            graph.append(single_line)
    
    return graph_details, graph



def knapsack_big():
    table = np.pad(np.zeros((graph_details[0], graph_details[1])), (0,1), 'constant')
    
    for j in range(1, graph_details[1] + 1):
#        print('j', j)
        value = graph[j-1][0]
        weight = graph[j-1][1]

        for i in range(1, graph_details[0] + 1):
#            print(i)
            if weight > i:
                table[i,j] = table[i,j-1]
            else:
                table[i,j] = max(table[i,j-1], table[i-weight, j-1] + value)

    return table[graph_details][0][-1]


import time
start_time = time.time()

graph_details, graph = create_graph('knapsack1.txt') 
#2493893

#graph_details, graph = create_graph('knapsack_big.txt') 
#4243395

#graph_details, graph = create_graph('test_cases/test4.txt') 
#147

#graph_details, graph = create_graph('test_cases/test2.txt') 
#5399

#graph_details, graph = create_graph('test_cases/test6.txt') 
#539


print('end', knapsack_big())


print("--- %s seconds ---" % (time.time() - start_time))