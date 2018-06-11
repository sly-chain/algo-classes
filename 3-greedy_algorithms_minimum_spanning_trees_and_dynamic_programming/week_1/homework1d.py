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




def find_parent(v):
    if parent[v] != v:
        find_parent(parent[v])
    return parent[v]


def update_parent(v, n):
    v_root = find_parent(v)
    n_root = find_parent(n)
    
    if rank[n_root] < rank[v_root]:
        parent[n_root] = v_root
        
    else:
        parent[v_root] = n_root
        if rank[v_root] == rank[n_root]:
            rank[v_root] += 1



def kruskal():
    iteration = 0
    i = 0
    result = []
    
#    while iteration < graph_details[0]-1:
#        print('iteration', iteration)
    while iteration < graph_details[0]-1:
        print(iteration)
        subset = graph[i]
        i += 1
        root_1 = find_parent(subset[1])
        root_2 = find_parent(subset[2])
#        print('roots', root_1, root_2)
        
        if root_1 != root_2:
            result.append(subset[0])
            iteration += 1
            update_parent(subset[1], subset[2])
#            print('parent', parent, '\n', 'rank', rank)
            
    return sum(result)
    

graph_details, graph = create_graph('edges.txt')    
parent = {elem:elem for elem in range(1, graph_details[0] + 1)}
rank = {elem:0 for elem in range(1, graph_details[0] + 1)}
print(kruskal())


#graph_details = [5, 10]
#graph = [[4, 2, 3], [5, 0, 3], [6, 0, 2], [10, 0, 1], [15, 1, 3]]
#parent = [elem for elem in range (0,4)]
#rank = [0 for elem in range (0,4)]
#print(kruskal())
    
    
    