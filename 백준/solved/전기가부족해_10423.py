import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
plants = list(map(int, input().split()))
link = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    link[u].append((w,v))
    link[v].append((w,u))
    
h = []
heapq.heapify(h)

visited = [0]*(N+1)
for plant in plants:
    visited[plant] = 1
    for elem in link[plant]:
        heapq.heappush(h, elem)
     
     
answer = 0 
   
while h:
    cost, nxt = heapq.heappop(h)
    if not visited[nxt]:
        visited[nxt] = 1
        answer += cost
        
        for nxt_cost, nxt_v  in link[nxt]:
            if not visited[nxt_v]:
                heapq.heappush(h, (nxt_cost, nxt_v))
                
print(answer)
        
    