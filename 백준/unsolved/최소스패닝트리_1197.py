import heapq
from sys import stdin

input = stdin.readline

n,e = map(int, input().split())

visited = [False for _ in range(n)]

h = []
for _ in range(e):
    n1,n2,w = map(int, input().split())
    h.append([w,n1,n2])
    
heapq.heapify(h)

answer = 0
while h:
    w,n1,n2 = heapq.heappop(h)
    if visited[n1-1] == False or visited[n2-1] == False:
        visited[n1-1] = True
        visited[n2-1] = True
        answer += w
print(answer)
