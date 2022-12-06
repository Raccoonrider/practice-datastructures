from sys import stdin

size = int(stdin.readline())
n = [int(x) for x in stdin.readline().split(" ")]

def valid_heap(numbers):
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] < numbers[i//2]:
            return False
    return True

swaps = []
for i in range(size//2+1, -1, -1):
    while i < size:
        m = i
        l = i * 2 + 1
        r = i * 2 + 2
        if l < size and n[l] < n[m]:
            m = l
        if r < size and n[r] < n[m]:
            m = r
        if m == i:
            break
        n[i], n[m] = n[m], n[i]
        swaps.append((m, i))
        i = m
        
print(len(swaps))
for s in swaps:
    print(s[0], s[1])