from sys import stdin, setrecursionlimit
from collections import deque


setrecursionlimit(10**8)
input = stdin.readline

n = int(input())
#인접 노드
adj = [[] for _ in range(n+1)]
#각 노드별 지름, 반지름 값 저장
rd = [[0,0]]*(n+1)


for _ in range(1, n):
    n1,n2,w = map(int, input().split())
    adj[n1].append([n2,w])
    
def dfs(node):
    if len(adj[node]) == 0:
        return rd[node]
    else:
        radius = []
        diameter = 0
        for nn, nw  in adj[node]:
            child_rd = dfs(nn)
            if len(radius) < 2:
                radius.append(child_rd[1]+nw)
                radius.sort(reverse=True)
            else:
                if radius[1] < child_rd[1]+nw:
                    radius[1] = child_rd[1]+nw
                    radius.sort(reverse=True)
            diameter = max(diameter, child_rd[1]+nw)
        rd[node] = [sum(radius),diameter]
        return rd[node]
    
    
dfs(1)
answer = 0
for radi ,dia in rd:
    if radi > answer:
        answer = radi

print(answer)
