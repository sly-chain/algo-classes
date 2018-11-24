import copy

class Node:
    def __init__(self, head, tail, weight):
        self.head = head
        self.tail = tail
        self.weight = weight
        self.parent = None


class Graph:
    def __init__(self, file):
        self.file = file
        self.v_total, self.e_total, self.graph, self.v_dict, self.v_list = self.create_graph()
        self.updated_graph = self.add_vertex()
        self.weighted_graph, self.weights = self.bellman_ford()

    def create_graph(self):
        graph = {}
        v_set = set()
        v_dict = {}
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = [int(s) for s in first_line.split()]
            v_total = graph_details[0]
            e_total = graph_details[1]
            
            for line in adjacency_list:
                l = [int(s) for s in line.split()]
                
                v_set.add(l[0])
                v_set.add(l[1])
                graph[(l[1], l[0])] = l[2]
                n = Node(l[1], l[0], l[2])
                
                if l[1] not in v_dict.keys():
                    v_dict[l[1]] = [n]
                else:
                    v_dict[l[1]].append(n)
            
            v_list = list(v_set)
        print('g', graph)
        return v_total, e_total, graph, v_dict, v_list


    def add_vertex(self):
        updated_graph = copy.deepcopy(self.graph)

        for v in self.v_list:
            updated_graph[(0, v)] = 0
        
        return updated_graph


    def bellman_ford(self):
        weights = {i: float('Inf') for i in self.v_list}
        # needs to be a list of all the vertices 
        weights[self.v_total+1] = 0
        weighted_graph = {}
        
        for i in self.v_total:
            for edge, distance in self.updated_graph.items():
                new_weight = weights[node.head] + node.weight
                if weights[node.tail] > new_weight:
                    weights[node.tail] = new_weight
                    
        #negative cycle check
        for node in self.updated_graph:
            if weights[node.head] + node.weight < weights[node.tail]:
                raise Exception('Graph contains negative weight cycle')
                return
        
        for u, v in self.updated_graph:
            if u != self.v_total:
                weighted_graph[(u, v)] = self.updated_graph[(u,v)] + weights[u] - weights[v]
        
        return weighted_graph, weights



import heapq
def dijkstra(weighted_graph, dist, v_list, v_dict, source):
    heap_map = {i: float('Inf') for i in v_list}
    parent = {i: None for i in v_list}
    heap_map[source] = 0
    heap_que = [(source, 0)]
    dist_map = {}
    
    while heap_que:
        current = heapq.heappop(heap_que)[0]
        dist_map[current] = heap_map[current]
        
        for node in v_dict[current]:
            if node.tail not in dist_map:
                continue
            
            new_weight = heap_map[current] + node.weight
                
            if heap_map[node.tail] > new_weight:
                heapq.heappush(heap_que, (node.tail, new_weight))
                node.parent = current
            
                    
    if dist_map:
        u = min(dist_map)
        v = parent[u]
        min_dist = dist_map[u]
        return min_dist - dist[u] + dist[v]
    
    print(min_dist)
    return


def johnson(g):
#    v_total, edges, graph, v_list = create_graph(file)
#    update_graph = add_vertex(v_total, graph)
#    weighted_graph, dist = bellman_ford(v_total+1, v_list, update_graph)
    results = []
    
    for source in g.v_list:
        solution = (dijkstra(g.weighted_graph, g.weights, g.v_list, g.v_dict, source))
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