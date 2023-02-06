from sys import stdin
from collections import defaultdict, deque

input = stdin.readline
N, M = map(int, input().split())
queue = []
phase = [0]*(N+1)
links = defaultdict(set)

for i in range(M):
    n1, n2 = map(int, input().split())
    links[n2].add(n1)
    phase[n1] += 1
    
q = deque([])

for i in range(1, N+1):
    if phase[i] == 0:
        q.append(i)
        
while q:
    crnt = q.popleft()
    queue.append(crnt)
    
    for nxt in links[crnt]:
        phase[nxt] -= 1
        if phase[nxt] == 0:
            q.append(nxt)
    
print(*queue[::-1])
