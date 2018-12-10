"""
In this assignment we will revisit an old friend, the traveling salesman problem (TSP). This week you will implement a heuristic for the TSP, rather than an exact algorithm, and as a result will be able to handle much larger problem sizes. Here is a data file describing a TSP instance (original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).

nn.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance \sqrt{(x-z)^2 + (y-w)^2} between them.

You should implement the nearest neighbor heuristic:

Start the tour at the first city.
Repeatedly visit the closest city that the tour hasn't visited yet. In case of a tie, go to the closest city with the lowest index. For example, if both the third and fifth cities have the same distance from the first city (and are closer than any other city), then the tour should begin by going from the first city to the third city.
Once every city has been visited exactly once, return to the first city to complete the tour.
In the box below, enter the cost of the traveling salesman tour computed by the nearest neighbor heuristic for this instance, rounded down to the nearest integer.

[Hint: when constructing the tour, you might find it simpler to work with squared Euclidean distances (i.e., the formula above but without the square root) than Euclidean distances. But don't forget to report the length of the tour in terms of standard Euclidean distance.]
"""

from math import sqrt


class Graph:
    def __init__(self, file):
        self.file = file
        self.total_coords, self.coords_list = self.create_graph()
        self.dist_matrix = self.distance_matrix()
    
    def create_graph(self):
        coords_list = []
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            total_coords = int(first_line)
    
            for line in adjacency_list:
                single_line = [float(s) for s in line.split()]
                coord1 = single_line[1]
                coord2 = single_line[2]
                coords_list.append((coord1, coord2))
                
        print("create graph--- %s seconds ---" % (time.time() - start_time))
        return total_coords, coords_list
        
    
    def calc_distance(self, x, y):
        dist = [(a - b)**2 for a, b in zip(x, y)]
        return sqrt(sum(dist))
    
    
    def distance_matrix(self):
        '''
        create matrix 
        returning coordinates (by indexes) and corresponding length
        sort matrix by length
        '''
        from collections import OrderedDict
        matrix = {}

# =============================================================================
#         for i in range(self.total_coords-1):
#             for j in range(i+1,self.total_coords):
#                 x = self.coords_list[i]
#                 y = self.coords_list[j]
#                 matrix[i,j] = self.calc_distance(x, y)
#                 matrix[j,i] = matrix[i,j]
#         
#         print("dist matrix--- %s seconds ---" % (time.time() - start_time))
# #        print(OrderedDict(sorted(matrix.items(), key=lambda x: x[1])))
#         return OrderedDict(sorted(matrix.items(), key=lambda x: x[1]))
# =============================================================================

        import numpy as np
        import itertools
         
        combos = np.array(list(itertools.permutations(range(self.total_coords), 2)))
         
        for i, j in combos:
            x = self.coords_list[i]
            y = self.coords_list[j]
            matrix[i,j] = self.calc_distance(x, y)
        
        print("dist matrix--- %s seconds ---" % (time.time() - start_time))
        return OrderedDict(sorted(matrix.items(), key=lambda x: x[1]))
        


def nearest(current, unvisited, dist_matrix):
    '''
    find nearest neighbor to the current coordinate 
    '''
    neighbor = unvisited[0]
    min_dist = dist_matrix[current, neighbor]
    
    for i in unvisited[1:]:
        if dist_matrix[current, i] < min_dist:
            min_dist = dist_matrix[current, i]
            neighbor = i
            
    return neighbor, min_dist


def tsp_nn(source):
    '''
    returns total length of path
    path as a roundtrip, returning to the source
    '''
    path = [source]
    current = source
    total = 0
    unvisited = list(range(g.total_coords))
    unvisited.remove(source)
    
    while unvisited != []:
        neighbor, min_dist = nearest(current, unvisited, g.dist_matrix)
        total += min_dist
        current = neighbor
        path.append(neighbor)
        unvisited.remove(neighbor)
    
    total += g.dist_matrix[path[-1], path[0]]
#    print(path, total)
    return round(total)


# =============================================================================
# def main():
#     '''
#     iterate through all coordinates and return minimum length path
#     '''
#     solutions = []
#     
#     for c in range(g.total_coords):
#         result, path = tsp_nn(c)
#         solutions.append(result)
#         
# #    print(solutions.index(min(solutions)))
#     return round(min(solutions))
# =============================================================================
    
    
import time
start_time = time.time()

g = Graph('nn.txt')
# =============================================================================
# #50 == 2470
#--- 0.38673925399780273 seconds ---
# 
# #1000 == 48581
#--- 7.9459052085876465 seconds ---
# 
# #last city is 18811
# =============================================================================


#g = Graph('test_cases/test1.txt')
# #23
#--- 0.001405954360961914 seconds ---
# =============================================================================


#g = Graph('test_cases/test2.txt')
# #83
#--- 0.0056531429290771484 seconds ---
# =============================================================================


#g = Graph('test_cases/test3.txt')
# #20638
#--- 5.0865867137908936 seconds ---
# =============================================================================

print(tsp_nn(0))
#print(main())    
print("--- %s seconds ---" % (time.time() - start_time))    
    
    
    