"""
In this programming problem and the next you'll code up the knapsack algorithm from lecture.

Let's start with a warm-up. Download the text file below.
knapsack1.txt

This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
"""

def create_graph(file):
    wt = []
    val = []
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        graph_details = [int(s) for s in first_line.split()]
            
        for line in adjacency_list:
            single_line = [int(s) for s in line.split()]
            val.append(single_line[0])
            wt.append(single_line[1])
    
    return graph_details[0], wt, val, graph_details[1]



def knapsack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapsack(W , wt , val , n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapsack(W-wt[n-1] , wt , val , n-1),
                   knapsack(W , wt , val , n-1))
    
    

import time
start_time = time.time()

#W, wt, val, n = create_graph('knapsack1.txt') 
#2493893

#W, wt, val, n = create_graph('test_cases/test1.txt') 
#147

#W, wt, val, n = create_graph('test_cases/test2.txt') 
#5399

W, wt, val, n = create_graph('test_cases/test3.txt') 
#539
#--- 38964.62129735947 seconds ---

print('end', knapsack(W, wt, val, n))


print("--- %s seconds ---" % (time.time() - start_time))