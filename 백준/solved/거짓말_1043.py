from sys import stdin
from collections import deque

input = stdin.readline

def out(gp):
    for row in gp:
        print(row)

n,m = map(int, input().split())
observer = list(map(int, input().split()[1:]))
parties = [[] for _ in range(m)]
gp = [set() for _ in range(n+1)]
knows = [0]*(n+1)

for i in range(m):
    guest = list(map(int, input().split()[1:]))
    parties[i].extend(guest)
    for i in range(len(guest)-1):
        
        gp[guest[i]].add(guest[i+1])
        gp[guest[i+1]].add(guest[i])
        

        
for i in observer:
    crnt = i
    knows[crnt] = 1
    q = deque(list(gp[i]))
    
    while q:
        nxt = q.popleft()
        if knows[nxt] == 0:
            knows[nxt] = 1
            q.extend(list(gp[nxt]))

answer = m
for i in range(len(parties)):
    for g in parties[i]:
        if knows[g] == 1:
            answer -= 1
            break
    
print(answer)

    
    
    