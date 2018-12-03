import copy

class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.parent = None

    def __lt__(self, other):
        return self.weight < other.weight

class Edge:
    def __init__(self, head, tail, weight):
        self.head = head
        self.tail = tail
        self.weight = weight

class Graph:
    def __init__(self, file):
        self.file = file
        self.v_dict, self.v_list, self.n_list = self.create_graph()
        self.updated_graph = self.add_vertex()
        self.weighted_graph, self.weights = self.bellman_ford()

    def create_graph(self):
        """
        returns:
            # total number of vertices
            # total number of edges
            # dictionary of vertices with their tails and weights
            # list of all vertices by id
            # list of all edges
            # list of all nodes
        """
        
        e_list = []
#        n_list = []
        v_set = set()
        v_dict = {}
        
        with open(self.file) as adjacency_list:
#            first_line = adjacency_list.readline()
            adjacency_list.readline()
#            graph_details = [int(s) for s in first_line.split()]
#            v_num = graph_details[0]
#            edge_num = graph_details[1]
            
            for line in adjacency_list:
                l = [int(s) for s in line.split()]
                
                v_set.add(l[0])
                v_set.add(l[1])

                e = Edge(l[1], l[0], l[2])
                e_list.append(e)
                
                n = Node(l[0], l[2])
#                n_list.append(n)
                
                if l[1] not in v_dict.keys():
                    v_dict[l[1]] = [n]
                else:
                    v_dict[l[1]].append(n)
            
            v_list = list(v_set)
#        print('g', graph)
#        print('d', v_dict)
#        return v_num, edge_num, v_dict, v_list, e_list, n_list
        return v_dict, v_list, e_list


    def add_vertex(self):
        updated_graph = copy.deepcopy(self.v_dict)
        updated_graph[0] = []

        for v in self.n_list:
            n = Node(0, 0)
            updated_graph[0].append(n)
        return updated_graph


    def bellman_ford(self):
        weighted_graph = copy.deepcopy(self.updated_graph)
        weights = {i: float('Inf') for i in self.v_list}
        weights[0] = 0
        
        for v in weighted_graph.keys():
            for node in weighted_graph[v]:
                new_weight = weights[v] + node.weight
                if weights[node.vertex] > new_weight:
                    weights[node.vertex] = new_weight
                    node.parent = v
                    
        #negative cycle check
        for v in weighted_graph.keys():
            for node in weighted_graph[v]:
                if weights[v] + node.weight < weights[node.vertex]:
                    raise Exception('Graph contains negative weight cycle')
                    return
        
        for n in weighted_graph.keys():
            for node in weighted_graph[n]:
                if n != 0:
                    node.weight = node.weight + weights[n] - weights[node.vertex]
        print('w', weighted_graph)
        return weighted_graph, weights



import heapq
def dijkstra(weighted_graph, weights, n_list, v_dict, source):
    heap_map = copy.deepcopy(weighted_graph)
    heap_map[source] = 0
    dist_map = {}
    
    while heap_map:
        current = heapq.heappop(heap_map)
        dist_map[current.vertex] = heap_map[current.vertex]
        
        for node in weighted_graph[current]:
            new_weight = heap_map[current.head] + node.weight
                
            if heap_map[node.vertex] > new_weight:
                node.weight = new_weight
                node.parent = current
            
    if dist_map:
        u = min(dist_map)
        return u.weight - weights[u.vertex] + weights[u.parent]
    
#    print(min_dist)
    return


def johnson(g):
    results = []
    
    for source in g.v_dict.keys():
        solution = (dijkstra(g.weighted_graph, g.weights, g.n_list, g.v_dict, source))
        if solution:
            results.append(solution)
    
    return min(results)
    

import time
start_time = time.time()

g = Graph('test_cases/test1.txt')
#-41

#print(johnson('test_cases/test2.txt'))
#TODO returning -2853
#-3127

#print(johnson('test_cases/test3.txt'))
#negative weight cycle

#print(johnson('test_cases/test4.txt'))
#TODO returning -1173
#-1557


#print(johnson('g1.txt'))
#returning negative weight cycle


#print(johnson('g2.txt'))
#returning negative weight cycle


#print(johnson('g3.txt'))
# returning -5


#print(johnson('large.txt'))
#-6

print(johnson(g))

print("--- %s seconds ---" % (time.time() - start_time))