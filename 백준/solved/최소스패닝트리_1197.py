import heapq
from sys import stdin

input = stdin.readline

n,e = map(int, input().split())

visited = [0]*(n+1)
adj = [[] for _ in range(n+1)]


for _ in range(e):
    n1,n2,w = map(int, input().split())
    adj[n1].append([w,n2])
    adj[n2].append([w,n1])
    
visited[1] = 1
h = adj[1]
heapq.heapify(h)

answer = 0
while h:
    w, next = heapq.heappop(h)
    if visited[next]:
        continue
    else:
        answer += w
        visited[next] = 1
        for elem in adj[next]:
            heapq.heappush(h,elem)
        
print(answer)
        
    
