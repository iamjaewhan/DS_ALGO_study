from sys import stdin
import heapq


input = stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,c = map(int, input().split())
    adj[s].append([c,e])
    adj[e].append([c,e])

S, D = map(int, input().split())
INF = float('inf')

dist = [INF]*(n+1)
dist[S] = 0
h = adj[S]
heapq.heapify(h)

while h:
    w, next = heapq.heappop(h)
    
    if w < dist[next]:
        dist[next] = w
        for elem in adj[next]:
            heapq.heappush(h, [dist[next]+elem[0],elem[1]])

print(dist[D])