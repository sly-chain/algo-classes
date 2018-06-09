"""
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]




Kruskal MST

1. sort edges in ascending order
2. create V subsets of single elements
3. number of edges taken = V-1

4. pick smallest edge and increment index for next iteration
5. if new edge doesn't cycle, add, and then increment index, otherwise discard
    edge

6. results list = MST
"""

def create_graph(file):
    edges_graph = []
    
    with open(file) as adjacency_list:
        first_line = adjacency_list.readline()
        next(adjacency_list)
        for line in adjacency_list:
            single_line = [int(s) for s in line.split()]
            vertex = single_line[0]
            node = single_line[1]
            cost = single_line[2]
            
            edges_graph.append([cost, vertex, node])
            graph_details = [int(s) for s in first_line.split()]
    
    return graph_details, sorted(edges_graph)



def parent_update(parent_map, vertex):
    if parent_map[vertex] == vertex:
        return vertex
    return parent_update(parent_map, parent_map[vertex])


def kruskal():
    parent_map = {elem:elem for elem in range(1, (graph_details[0] + 1))}
    result = []
    
    for subset in graph:
#        print(subset)
        
        if parent_map[subset[1]] != parent_map[subset[2]]:
            result.append(subset)
            parent_map[subset[2]] = parent_update(parent_map, subset[1])
#            parent_map[subset[1]] = parent_update(parent_map, subset[1])
#        print(parent_map[subset[1]], parent_map[subset[2]])
    
    print(parent_map)
    
    return len(result)
    

graph_details, graph = create_graph('edges.txt')    
print(kruskal())
    
    
    
    
    