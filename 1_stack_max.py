from collections import deque
from sys import stdin

n = int(stdin.readline())

d = deque()
m = deque()

for _ in range(n):
    command = stdin.readline()
    if 'push' in command:
        arg = int(command.split(" ")[1])
        d.append(arg)
        m.append(max(arg, m[-1] if m else arg))
    if 'pop' in command:
        d.pop()
        m.pop()
    if 'max' in command:
        print(m[-1] if m else 0)