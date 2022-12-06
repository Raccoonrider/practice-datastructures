n = int(input())

tree = []
for _ in range(n):
    tree.append([int(x) for x in input().split(" ")])
    # key left right
  
p = []

def in_order(tree, i):
    if i == -1: return
    node = tree[i]
    in_order(tree, node[1])
    p.append(str(node[0]))
    in_order(tree, node[2])
  
def pre_order(tree, i):
    if i == -1: return
    node = tree[i]
    p.append(str(node[0]))
    pre_order(tree, node[1])
    pre_order(tree, node[2])
  
def post_order(tree, i):
    if i == -1: return
    node = tree[i]
    post_order(tree, node[1])
    post_order(tree, node[2])
    p.append(str(node[0]))
  
  
in_order(tree, 0)
print(" ".join(p))
p = []
pre_order(tree, 0)
print(" ".join(p))
p = []
post_order(tree, 0)
print(" ".join(p))
p = []