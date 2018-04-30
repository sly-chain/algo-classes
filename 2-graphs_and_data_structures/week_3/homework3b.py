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
        self.height = 0
        self.balance_factor = 0
    
    def set_height(self):
        if self == None:
            return 0
        else:
            return 1 + max((self.left.height if self.left != None else 0), 
                       (self.right.height if self.right != None else 0))
        
    def height(self):
        return 0 if self.root == None else self.root.set_height()
        
    def get_balance_factor(self):
        if self.left:
            self.balance_factor =+ 1
        elif self.right == None:
            self.balance_factor += -1
        
#        return self.left.height - self.right.height
            

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            print('self.balance', self.root.balance_factor)
        else:
            self.insert_key(self.root, key)
        
    def insert_key(self, current_node, key):
        if current_node.value < key:
            if current_node.left:
                self.insert_key(current_node.left, key)
            else:
                print('do you get here')
                current_node.left = Node(key)
                current_node.height += 1
                
        else:
            if current_node.right:
                self.insert_key(current_node.right, key)
            else:
                current_node.right = Node(key)
                current_node.height += 1
        print('height', current_node.value, ':',  current_node.height) 
                
    def right_rotation(self):
        new_root = self.root.left
        self.root.left = new_root.right
        new_root.right = self.root
        
        self.root.height = self.root.set_height()
        new_root.height = new_root.set_height()
        print('here_r', new_root.height)        
        return new_root
        
    def left_rotation(self):
        new_root = self.root.right
        self.root.right = new_root.left
        new_root.left = self.root
        
        self.root.height = self.root.set_height()
        new_root.height = new_root.set_height()
        
        print('here_l', new_root.height)
        return new_root
    
    def balance_tree(self):
        if self.root.balance_factor > 1:
            if self.root.left.left.height >= \
            self.root.left.right.height:
                new_root = self.right_rotation()
                
            else:
                self.root.left = self.left_rotation()
                self.root = self.right_rotation()
                
            return new_root
        
        if self.root.balance_factor < -1:
            if self.root.right.right.height >= \
            self.root.right.left.height:
                new_root = self.left_rotation()
                
            else:
                self.root.right = self.right_rotation()
                self.root = self.left_rotation()
            
            return new_root
        
        
    def return_treetop(self, tree, node_count, data_array):
        if node_count%2 == 0:
            median_height = (node_count - 1) // 2 
        else:
            median_height = (node_count) // 2
        print('median height', median_height)
        for key in data_array[:10]:
            if Node(key).height == median_height:
                return key

def find_median():
    data_array = create_data_array('Median.txt')
    median_array = []
    tree = BST()
    node_count = 1
    
    for node_val in data_array[:5]:
        print('NODE COUNT', node_count)
        tree.insert(node_val)
        node_count += 1
        tree.balance_tree()
        median = tree.return_treetop(tree, node_count, data_array[:10]) 
        median_array.append(median)
    
#    return sum(median_array)%10000
    
    
print(find_median())


