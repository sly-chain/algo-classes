from collections import defaultdict

class Graph():
    
    def __init__(self, file):
        self.file = file
        self.total_count, self.graph, self.reverse_graph = self.create_graph()
        
    def encode(self, x, y, total_count):
        if x < 0:
            x += total_count 
        if y < 0:
            y += total_count
        return x, y
        
    def create_graph(self):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        
        with open(self.file) as adjacency_list:
            first_line = adjacency_list.readline()
            total_count = int(first_line)
            
            for line in adjacency_list:
                single_line = [int(s) for s in line.split()]
                x, y = self.encode(single_line[0], single_line[1], total_count)
                
                graph[x].append(y)
                reverse_graph[y].append(x)
                
        return total_count, graph, reverse_graph


g = Graph('test_cases/test1.txt')
print(g.graph)