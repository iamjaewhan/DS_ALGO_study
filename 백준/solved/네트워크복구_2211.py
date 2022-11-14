import sys
import heapq

from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
links = defaultdict(list)
dist = [0]*(n+1)
selected = set()

for _ in range(m):
    v1, v2, w = map(int, input().split())
    links[v1].append((w, v2, v1))
    links[v2].append((w, v1, v2))
    
def dijkstra(start):
    visited = [False]*(n+1)
    h = links[start].copy()
    
    visited[start] = True
    heapq.heapify(h)
    
    while h:
        w, nxt, crnt = heapq.heappop(h)
        
        if not visited[nxt]:
            selected.add((crnt, nxt))
            dist[nxt] = w
            visited[nxt] = True
            
            for nxt_w, nxt_nxt, nxt_crnt in links[nxt]:
                heapq.heappush(h, (w+nxt_w, nxt_nxt, nxt_crnt))
    

dijkstra(1)

print(len(selected))
for v1, v2 in selected:
    print(v1, v2)

