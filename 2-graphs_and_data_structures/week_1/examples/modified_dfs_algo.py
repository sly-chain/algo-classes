def dfs_topsort(graph):  
# recursive dfs with additional list for order of nodes
    L = []                      
    color = { u : "white" for u in graph }
    found_cycle = [False]
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break
 
    if found_cycle[0]:           
        L = []                   
 
    L.reverse()                  
    return L                     
 
 
def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "gray":
            found_cycle[0] = True
            return
        if color[v] == "white":
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = "black"
    L.append(u)


graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }

order = dfs_topsort(graph_tasks)
 
for task in order:
    print(task)