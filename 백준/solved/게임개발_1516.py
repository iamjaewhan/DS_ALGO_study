import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

cost = [0]*(n+1)
seq = [[] for _ in range(n+1)]
cnt = [0]*(n+1)
T= [0]*(n+1)

for i in range(1,n+1):
    temp = list(map(int, input().split()[:-1]))
    cost[i] = temp[0]
    for fromnode in temp[1:]:
        seq[fromnode].append(i)
    cnt[i] = len(temp[1:])

q = deque([])

for ind in range(1,n+1):
    if cnt[ind] == 0:
        q.append([ind, cost[ind]])
        T[ind] = cost[ind]

while q:
    crnt,c_cost = q.popleft()
    
    for nxt in seq[crnt]:
        cnt[nxt] -= 1 
        T[nxt] = max(T[nxt],T[crnt]+cost[nxt])
        if cnt[nxt] == 0:
            q.append([nxt, T[nxt]])
            
for i in range(1,n+1):
    print(T[i])
            