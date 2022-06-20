import sys
from collections import deque


sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def dfs(crnt, turn):
    global answer
    visited[crnt] = 1
    sets[turn].add(crnt)
    for nxt in link[crnt]:
        if visited[nxt] == 0:
            dfs(nxt, (turn+1)%2)
        else:
            if nxt in sets[turn]:
                answer = 'NO'
       
    
k = int(input())


for _ in range(k):
    answer = 'YES'
    sets = [set(), set()]
    v, e = map(int, input().split())
    link = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        link[v1].append(v2)
        link[v2].append(v1)
        
    for i in range(1,v+1):
        if visited[i] == 0:
            dfs(i, 0)
    print(answer)
    
    

    