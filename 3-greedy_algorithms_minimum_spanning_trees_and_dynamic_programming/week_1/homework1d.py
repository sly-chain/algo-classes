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
        graph_details = [int(s) for s in first_line.split()]

        for line in adjacency_list:
            single_line = [int(s) for s in line.split()]
            vertex = single_line[0]
            node = single_line[1]
            cost = single_line[2]
            
            edges_graph.append([cost, vertex, node])
    
    return graph_details, sorted(edges_graph)




def find_parent(v):
    if parent[v] == v:
        return parent[v]
    return find_parent(parent[v])


def update_parent(v, n):
    v_root = find_parent(v)
    n_root = find_parent(n)
    
    if rank[n_root] < rank[v_root]:
        parent[n_root] = v_root
        
    elif rank[v_root] < rank[n_root]:
        parent[v_root] = n_root
        
    else:
        parent[n_root] = v_root
        rank[v_root] += 1



def kruskal():
    i = 0
    result = []
    
#    while i < graph_details[0]-1:
    for subset in graph:
#        print(subset)
        parent_1 = find_parent(subset[1])
        parent_2 = find_parent(subset[2])
        
        if parent_1 != parent_2:
            result.append(subset[0])
            i += 1
            update_parent(subset[1], subset[2])
            
    return sum(result)
    

graph_details, graph = create_graph('edges.txt')    
parent = {elem:elem for elem in range(1, graph_details[0] + 1)}
rank = {elem:0 for elem in range(1, graph_details[0] + 1)}
print(kruskal())
# -3612829


#graph_details = [4, 10]
#graph = [[4, 2, 3], [5, 0, 3], [6, 0, 2], [10, 0, 1], [15, 1, 3]]
#parent = {elem:elem for elem in range(0, graph_details[0])}
#rank =  {elem:0 for elem in range(0, graph_details[0])}
#print(kruskal())
    
    
    