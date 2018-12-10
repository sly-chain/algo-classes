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
                coords_list.append((single_line[0], (single_line[1], single_line[2])))
        
#        print(total_coords)
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
        matrix = []

        for i in range(self.total_coords-1):
#            print('\n', 'i', i)
            for j in range(i+1,self.total_coords):
                x = self.coords_list[i][1]
                y = self.coords_list[j][1]
                
                length = self.calc_distance(x, y)
                matrix.append(((i, j), length))
                matrix.append(((j, i), length))
    
        print("distance matrix--- %s seconds ---" % (time.time() - start_time))
        return sorted(matrix, key=lambda x: x[1])


def get_index(curr, i, dist_matrix):
    for x, y in list(enumerate(dist_matrix)):
            if y[0] == (curr, i):
                return x

def nearest(curr, unvisited, dist_matrix):
    '''
    find nearest neighbor to the current coordinate 
    '''
#    print(unvisited)
    c = g.coords_list[curr][1]
    neighbor = unvisited[0]
    n = g.coords_list[unvisited[0]][1]
    min_dist = g.calc_distance(c, n)
    
    for i in unvisited[1:]:
        idx = get_index(curr, i, dist_matrix)
        if dist_matrix[idx][1] < min_dist:
            min_dist = dist_matrix[idx][1]
            neighbor = i
#        print(curr, i, idx, neighbor)
            
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
    
    idx = get_index(path[-1], path[0], g.dist_matrix)
    total += g.dist_matrix[idx][1]
#    print(path, total)
    return round(total)


    
import time
start_time = time.time()

#g = Graph('nn.txt')
# =============================================================================
# #50 == 2470
# 
# #1000 == 48581
# 
# #last city is 18811
# =============================================================================


#g = Graph('test_cases/test1.txt')
# #23
#--- 0.0013799667358398438 seconds ---
# =============================================================================


#g = Graph('test_cases/test2.txt')
# #83
#--- 0.009680986404418945 seconds ---
# =============================================================================


g = Graph('test_cases/test3.txt')
# #20638
# =============================================================================

print(tsp_nn(0))
#print(main())    
print("--- %s seconds ---" % (time.time() - start_time))    
    
    
    