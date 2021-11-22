from sys import stdin
import heapq

n,e=map(int, stdin.readline().split())
answer=0
visited=[False for i in range(n)]
edges=[[] for i in range(n+1)]

for i in range(e):
    n1,n2,w=map(int,stdin.readline().split())
    edges[n1].append([w,n2])
    edges[n2].append([w,n1])





adj_edges=[]
heapq.heapify(adj_edges)
for edge in edges[1]:
    heapq.heappush(adj_edges,edge)
visited[0]=True

while False in visited:
    w,v=heapq.heappop(adj_edges)
    if visited[v-1]==False:
        answer+=w
        visited[v-1]=True
        for edge in edges[v]:
            heapq.heappush(adj_edges,edge)


print(answer)


    
