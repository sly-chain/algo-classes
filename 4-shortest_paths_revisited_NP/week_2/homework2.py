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


#from itertools import permutations

def get_min_cost(current_vertex, current_set):
    start = 0
    total_set = vertices[1:]
    
    if current_set == []:
        min_cost = dist_matrix[current_vertex][start] 
        return min_cost
    
    for current_vertex in vertices[:1]:
        del current_set[current_vertex]
        min_cost = dist_matrix[current_vertex][start] + get_min_cost(current_vertex, current_set)
    
    return min_cost 

def tsp(file): 
    solution = get_min_cost(A, current_vertex, k, n)
    return solution
    
n, vertices, dist_matrix = create_list(file)



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


#print(tsp('tsp.txt'))

print(tsp('test_cases/test1.txt'))
# TODO returning 10.81
# 12.36

#print(tsp('test_cases/test2.txt'))

