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
            graph_details = int(first_line)
    
            for line in adjacency_list:
                single_line = [float(s) for s in line.split()]
                coord1 = single_line[0]
                coord2 = single_line[1]
                coords_list.append((coord1, coord2))
        
        return graph_details, coords_list

    
    def calc_distance(self, x, y):
        dist = [(a - b)**2 for a, b in zip(x, y)]
        dist = sqrt(sum(dist))
        return dist
    
    
    def distance_matrix(self):
        from collections import OrderedDict
        dist_matrix = {}

        for i in range(self.total_coords-1):
            for j in range(i+1,self.total_coords):
                x = self.coords_list[i]
                y = self.coords_list[j]
                dist_matrix[i,j] = self.calc_distance(x, y)
                dist_matrix[j,i] = dist_matrix[i,j]

        return OrderedDict(sorted(dist_matrix.items(), key=lambda x: x[1]))

# =============================================================================
#         import numpy as np
#         import itertools
#         
#         matrix = np.array(list(itertools.permutations(range(self.total_coords), 2)))
#         
#         for i, j in matrix:
#             x = self.coords_list[i]
#             y = self.coords_list[j]
#             distance = self.calc_distance(x, y)
#             dist_matrix[i, j] = distance
#             dist_matrix[y, x] = dist_matrix[x, y]
# =============================================================================
        


def nearest(last, unvisited, dist_matrix):
    near = unvisited[0]
    min_dist = dist_matrix[last, near]
    
    for i in unvisited[1:]:
        if dist_matrix[last,i] < min_dist:
            near = i
            min_dist = dist_matrix[last, near]
    return near, min_dist
    

def tsp_nn(g, source):
    unvisited = list(range(g.total_coords))
    unvisited.remove(source)
    last = source
    total = g.dist_matrix[0][1] + g.dist_matrix[-1]
    
    while unvisited != []:
        near, min_dist = nearest(last, unvisited, g.dist_matrix)
        total += min_dist
        unvisited.remove(near)
        last = near
        
    return total    


def main(g):
    solutions = []
    for c in range(g.total_coords):
        min_solution = float('Inf')
        current = tsp_nn(g, c)
        if current < min_solution:
            min_solution = current
        solutions.append(min_solution)

    return int(min(solutions))
    
    
import time
start_time = time.time()

#g = Graph('nn.txt')


#g = Graph('test_cases/test1.txt')
#23
#returning 16
#--- 0.000614166259765625 seconds ---


#g = Graph('test_cases/test2.txt')
#83
#returning 67
#--- 0.002496004104614258 seconds ---


g = Graph('test_cases/test3.txt')
#20638
#returning 20103
#--- 133.34567999839783 seconds ---



print(main(g))    
print("--- %s seconds ---" % (time.time() - start_time))    
    
    
    