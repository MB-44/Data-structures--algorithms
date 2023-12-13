# 1 part - key | data
# 2 part - left child
# 3 part - right child

# Insert in binary tree

class BST:
    def __init__(self,key):
        self.key = key
        self.Lchild = None
        self.Rchild = None 
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.Lchild:
                self.Lchild.insert(data)
            else: 
                self.Lchild = BST(data)
        else: 
            if self.Rchild:
                self.Rchild.insert(data)
            else: 
                self.Rchild = BST(data)

root = BST(10)
