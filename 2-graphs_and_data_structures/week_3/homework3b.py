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
        return 1 + max((self.left.height if self.left else 0), 
                       (self.right.height if self.right else 0))
        
    def get_balance_factor(self):
        return self.set_balance_factor() if self else 0
    
    def set_balance_factor(self):
        return (self.left.height if self.left else -1) - \
               (self.right.height if self.right else -1)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self.insert_key(self.root, key)
        else:
            self.root = Node(key)
            
        
    def insert_key(self, current_node, key):
        print('insert key for', current_node.value)
        if key < current_node.value:
            if current_node.left:
                self.insert_key(current_node.left, key)
            else:
                current_node.left = Node(key)
                Node(key).parent = current_node                
                current_node.balance_factor += 1
                if not current_node.right:
                    current_node.height += 1
                self.balance_tree(current_node)
                
        if key > current_node.value:
            if current_node.right:
                self.insert_key(current_node.right, key)
            else:
                current_node.right = Node(key)
                Node(key).parent = current_node
                current_node.balance_factor -= 1
                if not current_node.left:
                    current_node.height += 1
                self.balance_tree(current_node)
        
    def balance_tree(self, current_node):
        balance = current_node.balance_factor
        
        if balance > 1:
            if current_node.left.balance_factor > 0:
                self.right_rotation()
            else:
                self.left_rotation()
                self.right_rotation()
#            return new_root
        
        if balance < 1:
            if current_node.right.balance_factor < 0:
                self.left_rotation()
            else:
                self.right_rotation()
                self.left_rotation()
#            return new_root  
               
    def right_rotation(self):
        new_root = self.root.left
        self.root.left = new_root.right
        new_root.right = self.root
        
#        self.root.parent = new_root
        print('here_r', new_root.balance_factor, new_root.left.balance_factor, new_root.right.value)        
#        return new_root
        
    def left_rotation(self):
        new_root = self.root.right
        self.root.right = new_root.left
        new_root.left = self.root
        
#        self.root.parent = new_root
        print('here_l', new_root.value, new_root.left.value)
#        return new_root
        
    def return_treetop(self, node_count, data_array):
        for key in data_array[:5]:
            if Node(key).parent == None:
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


