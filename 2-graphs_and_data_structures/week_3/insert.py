

def insert(self, key):
    if not self.root:
        self.root = Node(key)
    else:
        self.insert_key(self.root, key)
    
    
def insert_key(self, current_node, key):
    
    if current_node.value <= key:
        if current_node.left:
            self.insert_key(current_node.left, key)
            
        else:
            current_node.left = Node(key)
            current_node.left.height += 1
            
    else:
        if current_node.right:
            self.insert_key(current_node.right, key)
        else:
            current_node.right = Node(key)
            current_node.right.height += 1