from collections import deque
from sys import stdin

size = int(stdin.readline())
stream = [int(x) for x in stdin.readline().split(" ")]
window = int(stdin.readline())

d = deque()

for i, value in enumerate(stream):
    while d and d[0] <= i - window:
        d.popleft()
    while d and value > stream[d[-1]]:
        d.pop()
    d.append(i)
    
    if i - window >= -1:
        print(stream[d[0]], end=" ")