def create_graph(file):
    with open(file) as f:
        first_line = f.readline()
        graph_details = [int(s) for s in first_line.split()]
        graph = [map(int, line.split()) for line in f]
            
    return graph_details, graph


def memoized(f):
    memo_dict = {}

    def helper(x):
        if x not in memo_dict:            
            memo_dict[x] = f(x)
        return memo_dict[x]
    return helper



def knapsack():
    """
    Solve the knapsack problem by finding the most valuable
    subsequence of `items` subject that weighs no more than
    `maxweight`.

    `items` is a sequence of pairs `(value, weight)`, where `value` is
    a number and `weight` is a non-negative integer.

    `maxweight` is a non-negative integer.

    Return a pair whose first element is the sum of values in the most
    valuable subsequence, and whose second element is the subsequence.

    >>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    >>> knapsack(items, 15)
    (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    """

    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    @memoized
    def bestvalue(i, j):
        if i == 0: return 0
        value, weight = graph[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j),
                       bestvalue(i - 1, j - weight) + value)

    j = graph_details[0]
    result = []
    for i in range(graph_details[1], 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(graph[i - 1])
            j -= graph[i - 1][1]
    result.reverse()
    return bestvalue(graph_details[1], graph_details[0]), result


import time
start_time = time.time()



#graph_details, graph = create_graph('knapsack1.txt') 
#2493893
#--- 1.253927230834961 seconds ---

#graph_details, graph = create_graph('knapsack_big.txt') 
#4243395
#--- 5076.164584875107 seconds ---

graph_details, graph = create_graph('test_cases/test1.txt') 
#147
#--- 0.002542734146118164 seconds ---

#graph_details, graph = create_graph('test_cases/test2.txt') 
#5399
#--- 0.10226893424987793 seconds ---

#graph_details, graph = create_graph('test_cases/test3.txt') 
#539
#--- 0.01104593276977539 seconds ---


print('end', knapsack())


print("--- %s seconds ---" % (time.time() - start_time))

