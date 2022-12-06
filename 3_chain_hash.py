from sys import stdin

m = int(stdin.readline())
n = int(stdin.readline())
p = 1_000_000_007
x = 263

class HashTable:
    def __init__(self, size):
        self.size = size
        self.values = [[None, None] for _ in range(size)]
        # [None, None] : [child, value]
        
    def h(self, s):
        return sum(ord(c) * x ** i % p for i, c in enumerate(s)) % p % self.size
        
    def add(self, value):
        node = self.get(value)
        if node is None:
            index = self.h(value)
            node = self.values[index]
            self.values[index] = [node, value]
            #while None not in node:
            #    node = node[0]
            #if node[1] is None:
            #    node[1] = value
            #elif node[0] is None:
            #    node[0] = [None, value]
                   
    def get(self, value):
        index = self.h(value)
        node = self.values[index]
        while node[1] != value:
            if node[0] is not None:
                node = node[0]
            else:
                return None
        return node
    
    def rm(self, value):
        node = self.get(value)
        if node is not None:
            node[1] = None
            
    def find(self, value):
        print(['yes', 'no'][int(self.get(value) is None)])
    
    def check(self, index):
        node = self.values[index]
        buffer = []
        while node is not None:
            if node[1] is not None:
                buffer.append(node[1])
            node = node[0]
        print (" ".join(buffer))
            
            
table = HashTable(m)
for _ in range(n):
    command, *args = input().split(" ")
    
    if command == 'add':
        table.add(args[0])
        
    if command == 'del':
        table.rm(args[0])
        
    if command == 'find':
        table.find(args[0])
        
    if command == 'check':
        table.check(int(args[0]))
        
