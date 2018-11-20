"""
In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance.


The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance \sqrt{(x-z)^2 + (y-w)^2} between them.

In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here. The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

Hint: You might experiment with ways to reduce the data set size. For example, trying plotting the points. Can you infer any structure of the optimal solution? Can you use that structure to speed up your algorithm?
"""


import numpy
from scipy.spatial.distance import pdist, squareform
from itertools import combinations, chain


def create_list(file):
    vertices = []
    
    with open(file) as vertex_list:
        total = int(vertex_list.readline())
        
        for line in vertex_list:
            vertices.append(([float(s) for s in line.split()]))
    
    coordinates_array = numpy.array(vertices)
    dist_array = pdist(coordinates_array)
    dist_matrix = squareform(dist_array)
    
    return total, vertices, dist_matrix


def create_powerset():
    s = range(1,n)
#    return list( map(list, chain.from_iterable((combinations(s, r) for r in range(len(s)+1))) ))
    return list(chain.from_iterable((combinations(s, r) for r in range(len(s)+1))))


def get_min_cost(subset, s, min_cost_dict):
    subset_copy = list(subset)
    subset_copy.remove(s)
    subset_copy = tuple(subset_copy)
    cost = min_cost_dict[s][subset_copy]
    return cost


def tsp(): 
    powerset = create_powerset()
    min_cost_dict = {k: {} for k in range(1, n)}

    for subset in powerset:
        for current in range(1, n):
            if current in subset:
                continue
            
            min_cost = float('Inf')
            for s in subset:
                cost = dist_matrix[s][current] + get_min_cost(subset, s, min_cost_dict)
                if cost < min_cost:
                    min_cost = cost
    
            if len(subset) == 0:
                min_cost = dist_matrix[0][current]
            
            min_cost_dict[current][subset] = min_cost
    
    return min_cost


import time
start_time = time.time()

n, vertices, dist_matrix = create_list('tsp.txt')
    

#n, vertices, dist_matrix = create_list('test_cases/test1.txt')
# 12.36

#n, vertices, dist_matrix = create_list('test_cases/test2.txt')
# 73

#n, vertices, dist_matrix = create_list('test_cases/test3.txt')
# 10.24

print(tsp())
print("--- %s seconds ---" % (time.time() - start_time))
#
#26368.1946948
#--- 5649.925425052643 seconds ---

# =============================================================================
# def generate_combinations(set_len):
#     combos = list(map(list, combinations(range(1, n), set_len)))
#     return combos 
# 
# def get_min_cost(current_set_len, A_prev):
#     A = numpy.array()
#     min_cost = float('Inf')
#     
#     combos = generate_combinations(current_set_len)
#     print(combos)
#     for c in combos:
#         vertex = c[0]
#         remaining_set = c[1:]
#         
#         for r in remaining_set:
#             cost = dist_matrix[vertex][r] + A_prev[r][remaining_set.remove(r)]
#             if cost < min_cost:
#                 min_cost = cost
#         
#         A[vertex][remaining_set] = min_cost
#     
#     return A
# =============================================================================


# =============================================================================
# from heapq import heappush, heappop
#from collections import namedtuple
#from math import sqrt

#def create_list(file):
#    cities = []
#    
#    with open(file) as city_list:
#        total = int(city_list.readline())
#        
#        for line in city_list:
#            cities.append(([float(s) for s in line.split()]))
#    
#    return total, cities

#def get_distance(start, end):
#    dist = [(a - b)**2 for a, b in zip(start, end)]
#    dist = sqrt(sum(dist))
#    return dist

    
# def tsp_prim(file):
#     n, cities = create_list(file)
#     
#     dist_map = {elem:float('Inf') for elem in range(len(cities))}
#     dist_map[0] = 0
#     
#     visited = []
#     source = 0
# #    HeapEntry = namedtuple('HeapEntry', 'distance node parent')
# #    source = HeapEntry(0, 0, None)
#     heap_que = [(0, (source, None))]
#     
# 
#     while heap_que:
# #        print(heappop(heap_que))
#         current = heappop(heap_que)[1][0]
#         visited.append(current)
#         
#         print(current)
#         for i in range(len(cities)):
#             if i not in visited:
#                 distance = get_distance(cities[current], cities[i])
#                 if distance < dist_map[i]:
#                     dist_map[i] = distance
#                     heappush(heap_que, (distance, (i, current)))
#     
#     return sum(dist_map.values())
# =============================================================================




