"""
In this programming problem and the next you'll code up the greedy algorithm from the lectures on Huffman coding.

Download the text file below.
huffman.txt

This file describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892. (We're using weights instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. What is the maximum length of a codeword in the resulting Huffman code?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

Continuing the previous problem, what is the minimum length of a codeword in your Huffman code?
"""


#1. Create a leaf node for each unique character and build a min heap of all leaf nodes (Min Heap is used as a priority queue. The value of frequency field is used to compare two nodes in min heap. Initially, the least frequent character is at root)

#2. Extract two nodes with the minimum frequency from the min heap.

#3. Create a new internal node with frequency equal to the sum of the two nodes frequencies. Make the first extracted node as its left child and the other extracted node as its right child. Add this node to the min heap. 


import heapq
import time

class Node:
    def __init__(self, symbol, weight, left, right):
        self.symbol = symbol
        self.weight = weight
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
        
        
    def __lt__(self, other):
        return self.weight < other.weight


class Huffman:
    def __init__(self, file):
        self.symbol_len, self.graph = self.create_graph(file)
        [self.root] = self.min_heap()
    
    
    def create_graph(self, file):
        graph = []
        
        with open(file) as adjacency_list:
            first_line = adjacency_list.readline()
            i = 1
            
            for line in adjacency_list:
#                single_line = int(line)
                node = Node(i, line, None, None)
                heapq.heappush(graph, node)
                i += 1
                
        return first_line, graph
    
    
    def min_heap(self):
        heap_que = self.graph[:]
        
        while len(heap_que) > 1:
            node1 = heapq.heappop(heap_que)
            node2 = heapq.heappop(heap_que)
            
            node = Node(None, node1.weight + node2.weight, node1, node2)
#            node.left = node1
#            node.right = node2
        
            heapq.heappush(heap_que, node)
            
        return heap_que
    
    
    def get_code(self, current, code):
        code = []
        if current.left:
#            print('left', current.left.symbol)
            code.append(0)
            self.get_code(current.left, code)
        
        if current.right:
#            print('right', current.right.weight)
            code.append(1)
            self.get_code(current.right, code)
            
        if current.is_leaf():
            return code
    
    
    def huffman(self):
        
        return self.get_code(self.root, [])
        

start_time = time.time()

#h = Huffman('test_cases/test1.txt')
#Min length = 2
#Max length = 5

h = Huffman('test_cases/test2.txt')
#Min length = 3
#Max length = 6

#h = Huffman('huffman.txt')

print('end', h.huffman())
print("--- %s seconds ---" % (time.time() - start_time))










