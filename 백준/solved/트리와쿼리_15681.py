import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
links = defaultdict(set)
dists = [0]*(N+1)
sub_nodes = [1]*(N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    links[u].add(v)
    links[v].add(u)
    
q = deque([(R,0)])
dists[R] = 0

while q:
    crnt, c_dist = q.popleft()
    
    for nxt in links[crnt]:
        if dists[nxt] == 0 and nxt != R:
            dists[nxt] = c_dist+1
            q.append((nxt, c_dist+1))


def get_subnodes(node):
    count = 1
    
    for nxt in links[node]:
        if dists[node] < dists[nxt]:
            count += get_subnodes(nxt)
            
    sub_nodes[node] = count
    return count
    

    
get_subnodes(R)
    
for _ in range(Q):
    print(sub_nodes[int(input())])