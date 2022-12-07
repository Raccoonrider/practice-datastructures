from heapq import heappush, heappop

text = input()

# Create heap of (frequency, character)
h = []
for x in set(text):
    heappush(h, (text.count(x), x))
    
# Populate binary tree of (characters, code)
# E.g. [('a', '0'), ('bc', '1'), ('b', '0'), ('c', '1')]
tree = []
if len(h) == 1:
    a = heappop(h)
    tree.append((a[1], "0"))
while len(h) > 1:
    a, b = heappop(h), heappop(h)
    heappush(h,(a[0] + b[0], a[1] + b[1]))
    tree.append((a[1], "0"))
    tree.append((b[1], "1"))

# Encode string: each time we see char in tree, add assosiated code
# E.g. for c in [('a', '0'), ('bc', '1'), ('b', '0'), ('c', '1')]: '11'
encoded = []
for letter in text:
    code = ""
    for node in tree:
        if letter in node[0]:
            code = node[1]+code
    encoded.append(code)
encoded = "".join(encoded)

print(f"{len(set(text))} {len(encoded)}")

# Print charmap
for letter in sorted(set(text)):
    code = ""
    for node in tree:
        if letter in node[0]:
            code = node[1]+code
    print(f"{letter}: {code}")
    
print(encoded)