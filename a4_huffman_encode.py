from heapq import heappush, heappop

text = input()

# Create heap of (frequency, character, subtree)
h = []
for x in set(text):
    heappush(h, (text.count(x), x, []))

if len(h) > 1:
    # Convert heap into tree
    while len(h) != 1:
        a, b = heappop(h), heappop(h)
        heappush(h,(
            a[0] + b[0], #frequency
            a[1] + b[1], #characters
            (a, b), #subtree
        ))
    tree = h[0][2]
else:
    tree = h

def encode(text):
    """Encode string"""
    encoded = []
    for letter in text:
        subtree = tree
        code = ""
        while subtree:
            if letter in subtree[0][1]:
                code += '0'
                subtree = subtree[0][2]
            elif letter in subtree[1][1]:
                code += '1'
                subtree = subtree[1][2]
            else:
                raise ValueError('Unexpected character')
        encoded.append(code)

    return "".join(encoded)

encoded = encode(text)

print(f"{len(set(text))} {len(encoded)}")

# Print charmap
for letter in sorted(set(text)):
    print(f"{letter}: {encode(letter)}")
    
print(encoded)