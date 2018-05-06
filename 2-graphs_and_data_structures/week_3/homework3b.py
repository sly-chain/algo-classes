def create_data_array(file):
    data_array = []
    with open(file) as f:
        data_array = list(map(int, f.read().splitlines()))
    return data_array


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  
        self.parent = None
        self.height = self.get_height()
        self.balance_factor = self.get_balance_factor()
    
    def get_height(self):
        return self.set_height() if self else 0

    def set_height(self):
        return 1 + max((self.left.height if self.left else -1), 
                       (self.right.height if self.right else -1))
        
    def get_balance_factor(self):
        return self.set_balance_factor() if self else 0
    
    def set_balance_factor(self):
        return (self.left.height if self.left else 0) - \
               (self.right.height if self.right else 0)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self.insert_key(self.root, key)
        else:
            self.root = Node(key)
            
        
    def insert_key(self, current_node, key):
        if key < current_node.value:
            if current_node.left:
                self.insert_key(current_node.left, key)
            else:
                current_node.left = Node(key)
                Node(key).parent = current_node  
                current_node.balance_factor += 1
#                if not current_node.right:
#                    current_node.height += 1
                self.balance_tree(current_node)
                
        if key > current_node.value:
            if current_node.right:
                self.insert_key(current_node.right, key)
            else:
                current_node.right = Node(key)
                Node(key).parent = current_node
                current_node.balance_factor -= 1
#                if not current_node.left:
#                    current_node.height += 1
                self.balance_tree(current_node)
    
# =============================================================================
#     def update_balance_factor(self, current_node):
#         if current_node.balance_factor > 1 or current_node.balance_factor < -1:
#             self.balance_tree(current_node)
#             return
#         if current_node.parent != None:
#             if current_node.isLeftChild():
#                 current_node.parent.balance_factor += 1
#             elif current_node.balance_factor():
#                 current_node.parent.balance_factor -= 1
#     
#             if current_node.parent.balance_factor != 0:
#                 self.update_balance_factor(current_node.parent)
# =============================================================================
    
    
    def balance_tree(self, current_node):
        balance = current_node.balance_factor
        
        if balance > 1:
            if current_node.left.balance_factor < 0:
                self.left_rotation(current_node.left)
                self.right_rotation(current_node)
            else:
                self.right_rotation(current_node)
        
        if balance < -1:
            if current_node.right.balance_factor > 0:
                self.right_rotation(current_node.right)
                self.left_rotation(current_node)
            else:
                self.left_rotation(current_node)
        
    def left_rotation(self, current_node):
        new_root = current_node.right
        new_root.left = current_node
        new_root.right = current_node.right.right
        
        current_node.parent = current_node.right.right.parent = new_root
        new_root.height = current_node.height
        
        print('here_L', current_node.value)
    
    def right_rotation(self, current_node):
        new_root = current_node.left  
        new_root.right = current_node 
        new_root.left = current_node.left.left
        
        current_node.parent = current_node.left.left.parent = new_root 
        new_root.height = current_node.height
        
        print('here_R', current_node.value, current_node.parent.value)        
    
    
    
    
# =============================================================================
#         A = self.node current_node
#         B = self.node.left.node 
#         T = B.right.node 
#         
#         self.node = B         A = B
#         B.right.node = A      B =   
#         A.left.node = T 
# =============================================================================
        
    def return_treetop(self, node_count, data_array):
        
        if node_count%2 == 0:
            median_height = node_count - 1//2
        else:
            median_height = node_count//2
        
        for key in data_array[:5]:
            if Node(key).height == median_height:
                return key

def find_median():
    data_array = create_data_array('Median.txt')
    median_array = []
    tree = BST()
    node_count = 1
    print('data array', data_array[:5], '\n')
    
    for node_val in data_array[:5]:
        tree.insert(node_val)
        print('\n', 'node:', Node(node_val).value)
        node_count += 1
        
        median = tree.return_treetop(node_count, data_array[:5]) 
        print('median:', median)
        median_array.append(median)
      
    return 'sum(median_array)%10000'
    
    
print(find_median())


