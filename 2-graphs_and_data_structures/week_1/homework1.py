"""
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0" (without the quotes). (Note also that your answer should not have any spaces in it.)

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
"""

# =============================================================================
# import sys
# import resource
# 
# #set rescursion limit and stack size limit
# sys.setrecursionlimit(10 ** 6)
# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
# =============================================================================

from operator import itemgetter 
from collections import defaultdict


# create represenation of graph as dictionary
def create_graph(file):
    graph = {}
    
    with open(file) as adjacency_list:
        for line in adjacency_list:
            single_line = [int(s) for s in line.replace(',', '').split()]
            graph[single_line[0]] = single_line[1:]
            
    return graph


def transpose_graph(graph):
    vertices = list(graph.keys())
    reverse_graph = defaultdict(list)
    
    for i in vertices:
        for v in graph[i]:
            reverse_graph[v].append(i)
    
    return reverse_graph

# explore nodes of graph 
# return dictionary of nodes and their respective finishing times
#   in descending order

def dfs(adj_list, start):
    """
    explore edges of specified node
    notes that node's finishing time
    
    returns:
        nothing
    """
    global explored, current_time, leader, finish_time, scc_list
    
    explored.append(start)
#    scc_list[leader].append(start)
    scc_list[leader] += 1
    
    for node in adj_list[start]:
        if node not in explored:
            dfs(adj_list, node)
    
    current_time += 1
    finish_time[start] = current_time
    

# loop through graph in ascending/descending order of nodes
# since dictionaries are unordered

def dfs_loop(adj_list, node_list):
    """
    input:
        graph - adjacency list
        node_list - specified order of nodes to be explored
    
    returns:
        nothing
    """
    
    global explored, current_time, leader, finish_time, scc_list
    
    explored = []
    current_time = 0
    leader = None
    finish_time = {}
#    scc_list = defaultdict(list)
    scc_list = defaultdict(int)
    

    for node in node_list:
       if node not in explored:
           leader = node
           dfs(adj_list, node)
    


def scc(graph, reverse_graph):
    reverse_node_list = sorted(graph.keys(), reverse=True)
    dfs_loop(reverse_graph, reverse_node_list)
    
    sorted_finish_time = [key for key, value in sorted(finish_time.items(), key = itemgetter(1), reverse = True)]
    
    dfs_loop(graph, sorted_finish_time)
    print(scc_list)

    leader_board = [value for key, value in sorted(scc_list.items(), key = itemgetter(1), reverse = True)]

    return leader_board[0:5]



graph = create_graph('SCC.txt')
#graph = {1:[4], 2:[8], 3:[6], 4:[7], 5:[2], 6:[9], 7:[1], 8:[5,6], 9:[3,7]}
#graph = {1:[2], 2:[3], 3:[1,5], 4:[5], 5:[6], 6:[4], 7:[6]}
reverse_graph = transpose_graph(graph)
print(scc(graph, reverse_graph))