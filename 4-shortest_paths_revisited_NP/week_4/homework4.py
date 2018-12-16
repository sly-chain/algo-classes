'''
The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not". For example, the second line of the first data file is "-16808 75250", which indicates the clause -x{16808} V x{75250}.

Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise. For example, if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string 111000 in the box below.

DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want. For example, 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per variable and two directed edges per clause, you should think through the details). This might be an especially attractive option for those of you who coded up an SCC algorithm in Part 2 of this specialization. Alternatively, you can use Papadimitriou's randomized local search algorithm. (The algorithm from lecture is probably too slow as stated, so you might want to make one or more simple modifications to it --- even if this means breaking the analysis given in lecture --- to ensure that it runs in a reasonable amount of time.) A third approach is via backtracking. In lecture we mentioned this approach only in passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, for example, for more details.
'''


from collections import defaultdict

class Graph():
    
    def __init__(self, file):
        self.file = file
        self.graph, self.reverse_graph = self.create_graph()
        self.total_count = 0
        
    def add_clause(self, x, y, total_count, graph):
        if x < 0:
            x += total_count 
        if y < 0:
            y += total_count
        graph[x].append(y)
        
    def add_inverse(self, x, y, total_count, reverse_graph):
        if x < 0:
            x += total_count 
        if y < 0:
            y += total_count
        reverse_graph[y].append(x)

    def create_graph(self):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            self.total_count = int(first_line)
            
            for line in adjacency_list:
                single_line = [int(s) for s in line.split()]
                x = single_line[0]
                y = single_line[1]
                
                self.add_clause(x, y, self.total_count, graph)
                self.add_inverse(x, y, self.total_count, reverse_graph)
                
        return graph, reverse_graph
            
    
def dfs():
    visited = []
    stack = []
    
    for node in g.graph:
        if node in visited:
            continue
        dfs_helper(node, visited, stack)

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
    scc = {}
    counter = 0
    
    while stack:
        node = stack.pop(0)
        reverse_dfs_helper(node, visited, scc, counter)
        counter += 1
    
#    print(scc)
    return scc

def reverse_dfs_helper(node, visited, scc, counter):
    visited.append(node)

    if node in g.reverse_graph:
        for v in g.reverse_graph[node]:
            if v in visited:
                continue
            reverse_dfs_helper(v, visited, scc, counter)
        
    scc[node] = counter


def sat():
    stack = dfs()
    scc = reverse_dfs(stack)
    
    for i in range(g.total_count):
        if scc[i] == scc[i + g.total_count]:
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

g = Graph('test_cases/test3.txt')
# =============================================================================
#0

print(sat())
print("--- %s seconds ---" % (time.time() - start_time)) 
