import copy

class Graph:

    def __init__(self, file):
        self.file = file
        self.v_total, self.graph, self.v_list, self.v_dict = self.create_graph()
        self.updated_graph = self.add_vertex()

    def create_graph(self):
        graph = []
        v_set = set()
        v_dict = {}
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = [int(s) for s in first_line.split()]
            v_total = graph_details[0]
            
            for line in adjacency_list:
                l = [int(s) for s in line.split()]
                
                v_set.add(l[0])
                v_set.add(l[1])
                
                e = Edge(l[1], l[0], l[2])
                graph.append(e)
                
                if l[1] not in v_dict.keys():
                    v_dict[l[1]] = [e]
                else:
                    v_dict[l[1]].append(e)
                

            v_list = list(v_set)
        return v_total, graph, v_list, v_dict


    def add_vertex(self):
        updated_graph = copy.deepcopy(self.graph)
        
        for v in self.v_list:
            e = Edge(0, v, 0)
            updated_graph.append(e)
        
        return updated_graph


class Edge:
    def __init__(self, head, tail, weight):
        self.head = head
        self.tail = tail
        self.weight = weight

    def __repr__(self):
        return 'Edge(%s)' % self.weight
    
    def __lt__(self, other):
        return self.weight < other.weight


def bellman_ford(v_total, v_list, updated_graph):
    dist = {i: float('Inf') for i in v_list}
    parent = {i: None for i in v_list}
    dist[0] = 0
    weighted_graph = []
    
    for i in range(v_total-1):
        for e in updated_graph:
            new_weight = dist[e.head] + e.weight
            if dist[e.tail] > new_weight:
                dist[e.tail] = new_weight
                parent[e.tail] = e.head
                
    #negative cycle check
    for e in updated_graph:
        if dist[e.head] + e.weight < dist[e.tail]:
            raise Exception('Graph contains negative weight cycle')
            return
    
    for e in updated_graph:
        if e.head != 0:
            weighted_graph.append(e) 
            e.weight = e.weight + dist[e.head] - dist[e.tail]
            
    return weighted_graph, dist



#import heapq
def dijkstra(weighted_graph, dist, v_list, v_dict, source):
#    heap_map = copy.deepcopy(weighted_graph)
#    heapq.heapify(heap_map)
    heap_map = {i: float('Inf') for i in v_list}
    heap_map[source] = 0
    parent = {i: None for i in v_list}
    dist_map = {}
    
    while heap_map:
        current = min(heap_map, key=heap_map.get)
        dist_map[current] = heap_map[current]
        heap_map.pop(current)
        
        if current in v_dict.keys():
            for e in v_dict[current]:
                if e.tail not in dist_map:
                    new_distance = dist_map[e.head] + e.weight
                            
                    if heap_map[e.tail] > new_distance:
                        heap_map[e.tail] = new_distance
                        parent[e.tail] = e.head
               
    if dist_map:
        u = min(dist_map)
        return dist_map[u]
#        v = parent[u]
#        if parent[u]:
#            min_dist = dist_map[u]
#            return min_dist - dist[u] + dist[v]
    
    return


def johnson(g):
#    v_total, edges, graph, v_list = create_graph(file)
#    update_graph = add_vertex(v_total, graph)
    weighted_graph, dist = bellman_ford(g.v_total+1, g.v_list, g.updated_graph)
    results = []
    
    for source in g.v_dict.keys():
        print('source', source)
        solution = (dijkstra(weighted_graph, dist, g.v_list, g.v_dict, source))
        results.append(solution)
    
    return min(x for x in results if x is not None)
    

import time
start_time = time.time()
#g = Graph('test_cases/test1.txt')
#-41

#g = Graph('test_cases/test2.txt')
#TODO returning -2853
#-3127

g = Graph('test_cases/test3.txt')
#negative weight cycle

#g = Graph(johnson('test_cases/test4.txt')
#TODO returning -1173
#-1557


#g = Graph(johnson('g1.txt')
#returning negative weight cycle


#g = Graph(johnson('g2.txt')
#returning negative weight cycle


#g = Graph(johnson('g3.txt')
# returning -5


#g = Graph(johnson('large.txt')
#-6

print(johnson(g))
print("--- %s seconds ---" % (time.time() - start_time))




