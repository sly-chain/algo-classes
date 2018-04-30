


def rotate_left(self):
    new_root = self.root.right
    self.root.right = new_root.left
    
    new_root.parent = self.root.parent
    self.root.parent = new_root
    new_root.left.parent = new_root
    
    if self.root.isRoot():
        self.root = new_root
    else:
        if self.root.isleft():
                self.root.parent.left = new_root
        else:
            self.root.parent.right = new_root
            
    new_root.left = self.root
    self.root.parent = new_root
    
    self.root.balanceFactor = self.root.balanceFactor + 1 - min(new_root.balanceFactor, 0)
    new_root.balanceFactor = new_root.balanceFactor + 1 + max(self.root.balanceFactor, 0)