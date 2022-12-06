import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, parent:'Node'=None):
        self.parent = parent
        self.value = value
        self.left_child = None
        self.right_child = None
        self.sum_tree = self.value

    def splay(self):
        while self.parent is not None:
            if self.parent.left_child is self:
                self.parent.sum_tree = (
                    self.parent.value 
                    + (self.parent.right_child.sum_tree if self.parent.right_child else 0)
                    + (self.right_child.sum_tree if self.right_child else 0)
                    )
                self.sum_tree = (
                    self.value
                    + (self.left_child.sum_tree if self.left_child else 0)
                    + self.parent.sum_tree
                )
                self.right_child, self.parent.left_child = self.parent, self.right_child
                if self.parent.left_child is not None:
                    self.parent.left_child.parent = self.parent
            elif self.parent.right_child is self:
                self.parent.sum_tree = (
                    self.parent.value 
                    + (self.parent.left_child.sum_tree if self.parent.left_child else 0) 
                    + (self.left_child.sum_tree if self.left_child else 0)
                    )
                self.sum_tree = (
                    self.value
                    + (self.right_child.sum_tree if self.right_child else 0)
                    + self.parent.sum_tree
                )
                self.left_child, self.parent.right_child = self.parent, self.left_child
                if self.parent.right_child is not None:
                    self.parent.right_child.parent = self.parent

            if self.parent.parent is not None:
                if self.parent.parent.left_child is self.parent:
                    self.parent.parent.left_child = self
                else:
                    self.parent.parent.right_child = self
            self.parent.parent, self.parent = self, self.parent.parent
        return self

    def search(self, n):
        result = self._search(n)
        return result, n == result.value

    def _search(self, n):        
        node = self
        while n != node.value:
            if n == node.value:
                return node.splay()
            elif n > node.value:
                if node.right_child is not None:
                    node = node.right_child
                else:
                    break
            elif n < node.value:
                if node.left_child is not None:
                    node = node.left_child
                else:
                    break    
        return node.splay() 
    

    def insert(self, n):
        node = self
        while n != node.value:
            if n == node.value:
                return node.splay()
            elif n > node.value:
                if node.right_child is not None:
                    node = node.right_child
                else:
                    node.right_child = Node(n, node)
                    return node.right_child.splay()
            elif n < node.value:
                if node.left_child is not None:
                    node = node.left_child
                else:
                    node.left_child = Node(n, node)
                    return node.left_child.splay() 
        return node.splay() 


    def remove(self, n):
        node = self._search(n)
        if node.value == n:
            if node.left_child is not None and node.right_child is not None:
                node.left_child.parent = None
                return node.left_child.merge(node.right_child)
            elif node.left_child:
                node.left_child.parent = None
                return node.left_child
            elif node.right_child:
                node.right_child.parent = None
                return node.right_child
            else:
                return None
        return node


    def split(self, n):
        if n == self.value:
            return self._split()
        if n > self.value:
            if self.right_child is not None:
                return self.right_child.split(n)
            else:
                return self._split()
        if n < self.value:
            if self.left_child is not None:
                return self.left_child.split(n)
            else:
                return self._split()

    def _split(self):
        self.splay()

        other = self.left_child
        self.left_child = None
        if other is not None:
            other.parent = None
        return other, self
    

    def merge(self, other:'Node'):
        node = self
        while node.right_child is not None:
            node = node.right_child
        node.splay()
        node.right_child = other
        node.sum_tree += other.sum_tree
        other.parent = node
        return node


    def sum(self, begin, end):
        root = self._search(begin)
        r = range(begin, end+1)
        result = 0

        if root.value in r:
            result += root.value
        node = root.right_child

        while node is not None:
            if node.value in r: 
                result += node.value
                if node.left_child:
                    s = node.left_child.sum_tree
                    result += s
                node = node.right_child
            else:
                node = node.left_child

        return root, result

    def _sum(self):
        value = self.value
        if self.left_child:
            value += self.left_child._sum()
        if self.right_child:
            value += self.right_child._sum()
        return value

n = int(input())
s = 0
tree = None
for _ in range(n):
    operation, *args = input().split(" ")
    
    if operation == "+":
        arg = (int(args[0]) + s) % 1_000_000_001
        if tree is None:
            tree = Node(arg)
        else:
            tree = tree.insert(arg)
            
    if operation == "-":
        arg = (int(args[0]) + s) % 1_000_000_001
        if tree is not None:
            tree = tree.remove(arg)
            
    if operation == "?":
        arg = (int(args[0]) + s) % 1_000_000_001
        if tree is not None:
            tree, result = tree.search(arg)
        if tree is not None and result:
            print("Found")
        else:
            print("Not found")
            
    if operation == "s":
        begin, end, *_ = [(int(x) + s) % 1_000_000_001 for x in args]
        if tree is not None:
            tree, s = tree.sum(begin, end)
        else:
            s = 0
        print(s)