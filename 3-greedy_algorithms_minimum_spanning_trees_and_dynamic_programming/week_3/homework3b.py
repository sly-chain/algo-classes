"""
In this programming problem you'll code up the dynamic programming algorithm for computing a maximum-weight independent set of a path graph.

Download the text file below.
mwis.txt

This file describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from lecture on this data set. The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set? (By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.) In the box below, enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise. For example, if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and the other four vertices are not, then you should enter the string 10011010 in the box below.
"""

import time

def create_path(file):
    path = []
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
            
        for line in adjacency_list:
            single_line = int(line.rstrip())
            path.append(single_line)
            
    return int(first_line), path


def create_set():
    A = {}
    A[-1] = 0
    A[0] = 0
    A[1] = path[0]
    
    for i in range(2, length):
        A[i] = max(A[i-1], A[i-2] + path[i-1])
        
    return A


def mwis(indices):
    result = []
    set = []
    i = len(A)-1
    
    while i >= 1:
        if A[i-1] >= A[i-2] + path[i-1]:
            i -= 1
        else:
            set.append(i)
            i -= 2
#    print(set)
    for x in indices:
        print(x)
        if x in set:
            result.append(1)
        else:
            result.append(0)
#        print(result)
    
    return result




start_time = time.time()
#length, path = create_path('mwis.txt')
#10100110

#length, path = create_path('test_cases/test3.txt')
#10010000

length, path = create_path('test_cases/test4.txt')
#10101100

A = create_set()
#A = [2, 9, 2, 9, 2, 9, 2, 9, 2, 9]
#A = [9, 2, 9, 2, 9, 2, 9, 2, 9, 2]

indices = [1, 2, 3, 4, 17, 117, 517, 997]

print(mwis(indices))
print("--- %s seconds ---" % (time.time() - start_time))




# =============================================================================
# 
# // Node count in the first element as per the file to be used 
# // in the question.
# 
# //Skip the first element then use every other
# int[] testCase3     = new int[]{10, 2, 9, 2, 9, 2, 9, 2, 9, 2, 9};
# int[] selectedNodes3= new int[]{ 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1};
# int   expectation3  = 45;
# 
# //Use the first element then skip every other
# int[] testCase4     = new int[]{10, 9, 2, 9, 2, 9, 2, 9, 2, 9, 2};
# int[] selectedNodes4= new int[]{ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0};
# int   expectation4  = 45;
# =============================================================================



