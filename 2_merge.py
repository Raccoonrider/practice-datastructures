from sys import stdin

_, requests = [int(x) for x in stdin.readline().split(" ")]

ranks = [int(x) for x in stdin.readline().split(" ")]
links = [i for i,_ in enumerate(ranks)]
max_rank = max(ranks)

def get_root(i):
    if i == links[i]:
        return i
    root = get_root(links[i])
    links[i] = root
    return root

for line in range(requests):
    dst, src = [int(x) - 1 for x in stdin.readline().split(" ")]

    dst = get_root(dst)
    src = get_root(src)
        
    if dst != src:
        ranks[dst] += ranks[src]
        links[src] = dst
        max_rank = max(max_rank, ranks[dst])

    print(max_rank)