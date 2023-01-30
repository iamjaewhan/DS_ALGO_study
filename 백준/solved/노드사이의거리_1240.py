import sys
from collections import defaultdict

input = sys.stdin.readline
N, Q = map(int, input().split())
links = defaultdict(list)

for _ in range(N-1):
    n1, n2, d= map(int, input().split())
    links[n1].append((d, n2))
    links[n2].append((d, n1))

def dfs(n1, dist):
    visited[n1] = dist
    
    for nxt_d, nxt in links[n1]:
        if visited[nxt] > nxt_d + dist:
            dfs(nxt, dist + nxt_d)
        



for _ in range(Q):
    
    visited = [float('inf')]*(N+1)
    n1, n2 = map(int, input().split())
    visited[n1] = 0    
    dfs(n1, 0)
    print(visited[n2])