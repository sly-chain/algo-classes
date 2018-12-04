import copy

class Graph:

    def __init__(self, file):
        self.file = file
        self.v_total, self.graph, self.edges = self.create_graph()
        self.updated_graph = self.add_vertex()
        self.dist, self.w_dict = self.bellman_ford()

    def create_graph(self):
        graph = {}
#        v_set = set()
        edges = []
#        v_dict = {}
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            graph_details = [int(s) for s in first_line.split()]
            v_total = graph_details[0]
            
            for line in adjacency_list:
                l = [int(s) for s in line.split()]
                
#                v_set.add(l[0])
#                v_set.add(l[1])
                
#                graph[l[1], l[0]] = l[2]
                e = Edge(l[1], l[0], l[2])
                edges.append(e)
                
                if l[1] not in graph.keys():
                    graph[l[1]] = [e]
                else:
                    graph[l[1]].append(e)
                
#            v_list = list(v_set)
            
        print("create--- %s seconds ---" % (time.time() - start_time))
        return v_total, graph, edges


    def add_vertex(self):
        updated_graph = copy.deepcopy(self.edges)
        
        for v in range(1, self.v_total+1):
            e = Edge(self.v_total+1, v, 0)
            updated_graph.append(e)
#        print('u', updated_graph)
        
        print("update--- %s seconds ---" % (time.time() - start_time))
#        print('u', updated_graph)
        return updated_graph


    def bellman_ford(self):
        dist = {i: float('Inf') for i in range(1, self.v_total+2)}
        dist[self.v_total+1] = 0
        weighted_graph = []
        w_dict = {}
        
        for i in range(self.v_total-1):
            for edge in self.updated_graph:
#                print('head', edge.head)
                new_weight = dist[edge.head] + edge.weight
                if dist[edge.tail] > new_weight:
                    dist[edge.tail] = new_weight
                    
        #negative cycle check
        for edge in self.updated_graph:
            if dist[edge.head] + edge.weight < dist[edge.tail]:
                raise Exception('Graph contains negative weight cycle')
                return
        
        for edge in self.edges:
            if edge.head != self.v_total+1:
                weighted_graph.append(edge) 
                edge.weight = edge.weight + dist[edge.head] - dist[edge.tail]
                
                if edge.head not in w_dict.keys():
                    w_dict[edge.head] = [edge]
                else:
                    w_dict[edge.head].append(edge)
        
        print(dist)
        print("bellman--- %s seconds ---" % (time.time() - start_time))            
        return dist, w_dict


class Edge:
    def __init__(self, head, tail, weight):
        self.head = head
        self.tail = tail
        self.weight = weight

    def __repr__(self):
        return 'Edge(%s, %s, %s)' % (self.head, self.tail, self.weight)
    
    def __lt__(self, other):
        return self.weight < other.weight


def dijkstra(dist, v_total, w_dict, source):
#    heap_map = copy.deepcopy(weighted_graph)
#    heapq.heapify(heap_map)
    heap_map = {i: float('Inf') for i in range(1, v_total+1)}
    heap_map[source] = 0
    parent = {i: None for i in range(1, v_total+1)}
    dist_map = {}
    
    while heap_map:
        current = min(heap_map, key=heap_map.get)
        dist_map[current] = heap_map[current]
        heap_map.pop(current)
        
        if current in w_dict.keys():
            for e in w_dict[current]:
                if e.tail in heap_map:
                    new_distance = dist_map[current] + e.weight
                            
                    if heap_map[e.tail] > new_distance:
                        heap_map[e.tail] = new_distance
                        parent[e.tail] = current
          
    if dist_map:
        print('dist', dist_map)
        tail = min(dist_map, key=dist_map.get)
        min_dist = dist_map[tail]
        head = parent[tail]
#        print(u, v)
        if head:
            return min_dist - dist[head] + dist[tail]
#    print("dijkstra--- %s seconds ---" % (time.time() - start_time)) 
    return


def johnson(g):
    results = []
    
    for source in g.w_dict.keys():
        solution = (dijkstra(g.dist, g.v_total, g.w_dict, source))
        if solution:
            results.append(solution)
#    print('results', results)
    return min(results)
    

import time
start_time = time.time()

g = Graph('test_cases/test1.txt')
#-41
#returning -41
#--- 0.0010831356048583984 seconds ---


#g = Graph('test_cases/test2.txt')
#-3127
#TODO returning -35
#--- 574.1097950935364 seconds ---

#g = Graph('test_cases/test3.txt')
#negative weight cycle

#g = Graph('test_cases/test4.txt')
#-1467
#TODO returning -70
#--- 9.257286071777344 seconds ---

#g = Graph('g1.txt')
#returning negative weight cycle
#TODO

#g = Graph('g2.txt')
#returning negative weight cycle
#TODO

#g = Graph('g3.txt')
#TODO returning -5


#g = Graph('large.txt')
#-6
#TODO

print(johnson(g))
print("--- %s seconds ---" % (time.time() - start_time))




