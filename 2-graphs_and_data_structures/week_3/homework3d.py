def create_data_array(file):
    data_array = []
    with open(file) as f:
        data_array = list(map(int, f.read().splitlines()))
    return data_array


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right  
        self.parent = parent
        self.balance_factor = 0
        
    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent
    

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
                current_node.left = Node(key, parent=current_node)
                
                self.update_balance_factor(current_node)
                
        if key > current_node.value:
            if current_node.right:
                self.insert_key(current_node.right, key)
            else:
                current_node.right = Node(key, parent=current_node)
                
                self.update_balance_factor(current_node)
#                if not current_node.left:
#                    current_node.height += 1
#                self.balance_tree(current_node)
        
        
    def balance_tree(self, current_node):
        balance = current_node.balance_factor
        print('BALANCE TREE-CURRENT NODE', current_node.value,
              current_node.balance_factor)
        
        if balance > 0:
            if current_node.left.balance_factor < 0:
                self.left_rotation(current_node.left)
            self.right_rotation(current_node)
        
        if balance < 0:
            if current_node.right.balance_factor > 0:
                self.right_rotation(current_node.right)
            self.left_rotation(current_node)
            
    def update_balance_factor(self, current_node):
        
        if current_node.balance_factor > 1 or current_node.balance_factor < -1:
            self.balance_tree(current_node)
            return
        
        if current_node.parent:
            if current_node.is_left():
                current_node.parent.balance_factor += 1
            elif current_node.is_right():
                current_node.parent.balance_factor -= 1
    
            if current_node.parent.balance_factor != 0:
                self.update_balance_factor(current_node.parent)
        
    
    def right_rotation(self, current_node):
        print('RIGHT-CURRENT NODE', current_node.value)
        new_root = current_node.left
        current_node.left = new_root.right
        
        if new_root.right:
            new_root.right.parent = current_node
    
        new_root.parent = current_node.parent
        
        if current_node.is_root():
            self.root = new_root
        else:
            if current_node.is_right():
                current_node.parent.right = new_root
            else:
                current_node.parent.left = new_root
    
        new_root.right = current_node
        current_node.parent = new_root
        current_node.balance_factor = current_node.balance_factor + 1 - \
        min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + \
        max(current_node.balance_factor, 0)
        
        print('here_r', new_root.value, new_root.right.value)        

        
    def left_rotation(self, current_node):
        print('LEFT-CURRENT NODE', current_node.value)
        new_root = current_node.right
        current_node.right = new_root.left
        
        if new_root.left:
            new_root.left.parent = current_node
    
        new_root.parent = current_node.parent
        
        if current_node.is_root():
            self.root = new_root
        else:
            if current_node.is_left():
                current_node.parent.left = new_root
            else:
                current_node.parent.right = new_root
    
        new_root.left = current_node
        current_node.parent = new_root
        current_node.balance_factor = current_node.balance_factor + 1 - \
        min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + \
        max(current_node.balance_factor, 0)
        
        print('here_l', new_root.value, new_root.left.value)

        
    def return_treetop(self, node_count, data_array):
        for key in data_array[:5]:
            if Node(key).is_root:
                return key
        
def find_median():
    data_array = create_data_array('Median.txt')
    print('data array', data_array[:5], '\n')
    
    median_array = []
    tree = BST()
    node_count = 1
    
    for node_val in data_array[:5]:
        tree.insert(node_val)
        node_count += 1
        print('\n', 'node:', Node(node_val).value, Node(node_val).parent)
        
        median = tree.return_treetop(node_count, data_array[:5]) 
        median_array.append(median)
        print(median_array)
        
    return 'sum(median_array)%10000'
    
    
print(find_median())


