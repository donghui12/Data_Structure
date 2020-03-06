
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

    def add_right(self,data):
        if self.right == None:
            self.right = Tree(data)
        else:
            self.right.add_right(data)

    def get_tree(self, treenode):
        if treenode is None:
            return ""
        print(treenode.root, end=" ")
        if treenode.left:
            self.get_tree(treenode.left)
        if treenode.right:
            self.get_tree(treenode.right)
        
        

if __name__=="__main__":
    tree = Tree(5)
    tree.add_left(4)
    tree.add_right(6)
    tree.add_left(3)
    print(tree.get_tree(tree))
