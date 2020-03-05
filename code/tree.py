
class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def get_root(self):
        return self.root
    
    def get_leftchild(self):
        return self.left

    def get_rightchild(self):
        return self.right

    def add_left(self, data):
        if self.left == None:
            self.left = Tree(data)
        else:
            self.left.add_left(data)

    def add_Right(self,data):
        if self.right == None:
            self.right = Tree(data)
        else:
            self.right.add_right(data)

    def get_tree(self):
        print(self.root, ' ', end="")
        if self.left == None and self.right == None:
            return self.root
        elif self.left == None:
            self.right.get_tree()
        else:
            self.left.get_tree()
        
        

if __name__=="__main__":
    tree = Tree(5)
    tree.add_left(4)
    tree.add_left(3)
    print(tree.get_root())
    print(tree.get_leftchild())
    print(tree.get_rightchild())
    print(tree.get_tree())
