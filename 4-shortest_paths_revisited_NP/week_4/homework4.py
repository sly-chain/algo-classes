'''
The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not". For example, the second line of the first data file is "-16808 75250", which indicates the clause -x{16808} V x{75250}.

Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise. For example, if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string 111000 in the box below.

DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want. For example, 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per variable and two directed edges per clause, you should think through the details). This might be an especially attractive option for those of you who coded up an SCC algorithm in Part 2 of this specialization. Alternatively, you can use Papadimitriou's randomized local search algorithm. (The algorithm from lecture is probably too slow as stated, so you might want to make one or more simple modifications to it --- even if this means breaking the analysis given in lecture --- to ensure that it runs in a reasonable amount of time.) A third approach is via backtracking. In lecture we mentioned this approach only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, for example, for more details.
'''


from collections import defaultdict

class Graph():
    
    def __init__(self, file):
        self.file = file
#        self.total_count, self.graph = self.create_graph()
#        self.reverse_graph = self.transpose_graph()
        self.total_count, self.graph, self.reverse_graph = self.create_graph()

    def create_graph(self):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            n = int(first_line)
            
            for line in adjacency_list:
                single_line = [int(s) for s in line.split()]
                x = single_line[0]
                y = single_line[1]
                
#                graph[-x].append(y)
#                graph[-y].append(x)
#                reverse_graph[y].append(-x)
#                reverse_graph[x].append(-y)
                if (x>0 and y>0):
                    graph[x+n].append(y)
                    graph[y+n].append(x) 
                    reverse_graph[y].append(x+n)
                    reverse_graph[x].append(y+n)
          
                elif (x>0 and y<0): 
                    graph[x+n].append(n-y)
                    graph[-y].append(x)
                    reverse_graph[n-y].append(x+n)
                    reverse_graph[x].append(-y)
          
                elif (x<0 and y>0):
                    graph[-x].append(y)
                    graph[y+n].append(n-x)
                    reverse_graph[y].append(-x)
                    reverse_graph[n-x].append(y+n)
          
                else:
                    graph[-x].append(n-y)
                    graph[-y].append(n-x)
                    reverse_graph[n-y].append(-x)
                    reverse_graph[n-x].append(-y)
                
#        print(graph)
#        print(reverse_graph)
        return n, graph, reverse_graph
    
# =============================================================================
#     def transpose_graph(self):
#         reverse_graph = defaultdict(list)
#         
#         for k, v in self.graph.items():
#             for i in v:
#                 reverse_graph[i].append(k)
# #        print(reverse_graph)
#         return reverse_graph
#         
# =============================================================================
    
def dfs():
    visited = []
    stack = []
    
#    for node in g.graph:
    for node in range(1, (2*g.total_count)+1):
        if node in visited:
            continue
        dfs_helper(node, visited, stack)
    
#    print(stack)
    return stack
    
def dfs_helper(node, visited, stack):
    visited.append(node)
    
    if node in g.graph:
        for v in g.graph[node]:
            if v in visited:
                continue
            dfs_helper(v, visited, stack)
            
    stack.append(node)
    
    
def reverse_dfs(stack):
    visited = []
    scc = defaultdict(list)
    counter = 0
    
    while stack:
        node = stack.pop(0)
#        print('n', node)
        if node not in visited:
            reverse_dfs_helper(node, visited, scc, counter)
            counter += 1
    
    print('scc', scc)
    return scc

def reverse_dfs_helper(node, visited, scc, counter):
    if node in visited:
        return
    
    visited.append(node)
#    print(node, scc)
    
    if node in g.reverse_graph:
        for v in g.reverse_graph[node]:
            reverse_dfs_helper(v, visited, scc, counter)
#        for v in g.reverse_graph[node]:
#            if v in visited:
#                continue
#            reverse_dfs_helper(v, visited, scc, counter)
        
    scc[node] = counter


def sat():
    stack = dfs()
    scc = reverse_dfs(stack)
    
#    for i in range(1, g.total_count+1):
#        if scc[i] == scc[-i]:
#            return 0
#    return 1

    for i in range(1, g.total_count+1):
#        print('i', i)
        if scc[i] == scc[i+g.total_count]:
            return 0
    return 1








import time
start_time = time.time()


#g = Graph('2sat1.txt')
#--- 420.0536332130432 seconds ---

#g = Graph('2sat2.txt')
#g = Graph('2sat3.txt')
#g = Graph('2sat4.txt')
#g = Graph('2sat5.txt')
#g = Graph('2sat6.txt')


#g = Graph('test_cases/test1.txt')
# =============================================================================
#0

#g = Graph('test_cases/test2.txt')
# =============================================================================
#1

#g = Graph('test_cases/test3.txt')
# =============================================================================
#0

g = Graph('test_cases/test4.txt')
# =============================================================================
#1

print('result', sat())
print("--- %s seconds ---" % (time.time() - start_time)) 
