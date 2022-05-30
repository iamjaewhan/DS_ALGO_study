from collections import deque
import sys

input= sys.stdin.readline

n = int(input())

gp = [[] for _ in range(n+1)]
candidates = [] 
points = float('inf')

while True:
    n1, n2 = map(int,input().split())
    if n1 == -1 and n2 == -1:
        break
    gp[n1].append(n2)
    gp[n2].append(n1)


for i in range(1,n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    q = deque([[i,0]])
    i_dist = 0
    while q:
        crnt, dist = deque.popleft(q)
        if dist > i_dist:
            i_dist = dist
        for nxt in gp[crnt]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append([nxt, dist+1])
    
    if i_dist < points:
        points = i_dist
        candidates = [i]
    elif i_dist == points:
        candidates.append(i)

print(points, len(candidates))
print(" ".join(str(num) for num in candidates))
    
    