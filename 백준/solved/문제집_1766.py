import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
depth = [0]*(N+1)
look = defaultdict(list)
answer = []


for _ in range(M):
    a,b = map(int, input().split())
    depth[b] += 1
    look[a].append(b)
    
h = []
heapq.heapify(h)

for i in range(1, N+1):
    if depth[i] == 0:
        heapq.heappush(h, i)
        
while h:
    crnt = heapq.heappop(h)
    answer.append(crnt)
    
    for nxt in look[crnt]:
        depth[nxt] -= 1
        if depth[nxt] == 0:
            heapq.heappush(h, nxt)


print(*answer)
    