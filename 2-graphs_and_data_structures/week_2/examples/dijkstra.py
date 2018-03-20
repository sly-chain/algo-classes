def dijkstra(self, start, end):

    graph = self.neighbours #{'A': {'B':2}, 'B': {'C':4}, ... }

    heap_map = {n: 1000 for n in self.graph} #heap_map node & distance
    heap_map[start] = 0 #set start vertex to 0
    distance_map = {} #list of all distance_map graph
    parent = {} #predecessors

    while heap_map:
        current = min(heap_map, key=heap_map.get) #get smallest distance

        for vertex in graph[current].items():
            if vertex not in distance_map:
                new_distance = heap_map[current] + graph[current][vertex]
                if new_distance < heap_map[vertex]:
                    heap_map[vertex] = new_distance
                    parent[vertex] = current

        distance_map[current] = heap_map[current]
        heap_map.pop(current)

    print(parent, distance_map)
    
    
    
    


import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.nodes = set(range(n))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}

    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path
