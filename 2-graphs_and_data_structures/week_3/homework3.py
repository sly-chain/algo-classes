"""
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (m1+m2+m3+⋯+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.
"""

from heapq import heappush

heap = []
ordered_array = []

def create_data_array(file):
    data_array = []
    
    with open(file) as f:
        data_array = list(map(int, f.read().splitlines()))
        
    return data_array


def find_median(data_array):
    median_array = []
    
    for item in data_array[:5]:
        heappush(heap, item)
        heap.sort()
        
        if len(heap)%2 == 0:
            median_item = heap[(len(heap) - 1)//2] 
        else:
            median_item = heap[len(heap)//2]
        
        median_array.append(median_item)
    
    print('medians', median_array)
    return sum(median_array)%10000



data_array = create_data_array('Median.txt')
print(find_median(data_array))


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None  
        self.height = 0
    
    def set_height(self):
        return 1 + max((self.left.height if self.left != None else 0), 
                       (self.right.height if self.right != None else 0))
        
    def height(self):
        return 0 if self.root == None else self.height
        
    
    def get_max_child_height(self):
            self.height = 1 + max(self.root.left_child.height,
                                   self.root.right_child.height)

    def get_balance_factor(self):
        if self.left_child == None or self.right_child == None:
            return 0
        
        else:
            return self.left_child.height - self.left.child.height
            

class BST:
    def __init__(self):
        self.root = None
        self.parent = None

    def insert_key(self, current_node, key):
        if not self.root:
            self.root = Node(key)
            
        else:
            if current_node.value <= key:
                if current_node.left_child:
                    self.insert_key(current_node.left_child, key)
                else:
                    current_node.left_child = Node(key)
                    current_node.left_child.height += 1
                    
            else:
                if current_node.right_child:
                    self.insert_key(current_node.right_child, key)
                else:
                    current_node.right_child = Node(key)
                    current_node.right_child.height += 1

    def right_rotation(self):
        new_root = self.root.left_child
        self.root.left_child = new_root.right_child
        self.root.left_child.parent = self.root
        
        new_root.right_child = self.root
        new_root.right_child.parent = new_root
        
        self.root.height = self.root.get_max_child_height()
        new_root.height = new_root.get_max_child_height()
        
        return new_root
        
    def left_rotation(self):
        new_root = self.root.right_child
        self.root.right_child = new_root.left_child
        new_root.left_child = self.root
        
        self.root.right_child.parent = self.root
        new_root.left_child.parent = new_root
        
        self.root.height = self.root.get_max_child_height()
        new_root.height = new_root.get_max_child_height()
        
        return new_root
        
    def balance_tree(self):
        self.root.balance_factor = self.root.get_balance_factor()
        
        if self.root.balance_factor > 1:
            if self.root.left_child.left_child.height >= \
            self.root.left_child.right_child.height:
                new_root = self.root.right_rotation()
                
            else:
                self.root.left = self.root.left_rotation()
                self.root = self.root.right_rotation()
                
            return new_root
        
        if self.root.balance_factor < -1:
            if self.root.right_child.right_child.height >= \
            self.root.right_child.left_child.height:
                new_root = self.root.left_rotation()
                
            else:
                self.root.right = self.root.right_rotation()
                self.root = self.root.left_rotation()
            
            return new_root
    
#    def update_parent(self, node):
#        if node.right_child:
#            node.right_child.parent = node.value
#        if node.left_child:
#            node.left_child.parent = node.value
        
    def return_median(self):
        if not self.parent:
            return self.root.value


#    def find_key(self, current_node, key):
#        if self.root == None:
#            return None
#        
#        else:
#            if current_node == key:
#                return current_node
#            
#            elif current_node < key:
#                self.find_key(current_node.right, key)
#                
#            elif current_node < key:
#                self.find_key(current_node.left, key)
    
    



#def create_data_array(file):
#    data_array = []
#    
#    with open(file) as f:
#        data_array = list(map(int, f.read().splitlines()))
#        
#    return data_array



def find_median():
    data_array = create_data_array('Median.txt')
    median_array = []
    tree = BST()
    root = data_array[0]
    
    for node_val in data_array[:5]:
        current_node = Node(root)
        tree.insert_key(current_node, node_val)
        tree.balance_tree()
#        tree.update_parent(current_node)
        
        median = tree.return_median() 
        median_array.append(median)
    
    print('medians', median_array)
    return sum(median_array)%10000
    
    
print(find_median())
    
    




