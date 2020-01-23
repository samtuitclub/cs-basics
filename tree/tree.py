class Node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.p = None

class Tree:

    def __init__(self):
        self.root = None

    def iterative_search(self, k):
        x = self.root
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self):
        x = self.root
        while x.left != None:
            x = x.left
        return x

    def maximum(self):
        x = self.root
        while x.right != None:
            x = x.right
        return x

    def successor(self):
        x = self.root
        if x.right != None:
            return minimum(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def insert(self, v):
        z = Node()
        z.key = v
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y


def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)

def tree_search(x, k):
    if x == None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

