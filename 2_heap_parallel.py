from heapq import heappush, heappop

size, _ = [int(x) for x in input().split(" ")]
tasks = [int(x) for x in input().split(" ")]

heap = []
t = 0
cpu = 0
for task in tasks:
    if len(heap) == size:
        done = heappop(heap)
        t = done[0]
        cpu = done[1]

    print(cpu, t)
    heappush(heap, (t+task, cpu))
    cpu += 1