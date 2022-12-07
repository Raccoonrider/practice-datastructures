k, l = [int(x) for x in input().split(" ")]
h = sorted([input().split(": ") for _ in range(k)], key= lambda x: (x[1], x[0]))

encoded = list(input())[::-1]
decoded = []
while encoded:
    buffer = encoded.pop()
    for char in h:
        while char[1].startswith(buffer) and char[1] != buffer:                
            buffer += encoded.pop()
        if char[1] == buffer:
            decoded.append(char[0])
            break
            
print("".join(decoded))