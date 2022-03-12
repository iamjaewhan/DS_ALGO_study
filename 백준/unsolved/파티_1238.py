from sys import stdin
import heapq

INF = float('inf')
input = stdin.readline

n,m,x = map(int, input().split())
gp = [[] for _ in range(n+1)]

for _ in range(m):
    s,d,t = map(int, input().split())
    gp[s].append([t,d])
    
dists = []
for i in range(1,n+1):
    dist = [INF]*(n+1)
    dist[i] = 0
    h = []
    h = gp[i]
    heapq.heapify(h)
    
    while h:
        t,d = heapq.heappop(h)
        if dist[d] > t:
            dist[d] = t
            for elem in gp[d]:
                nt = t + elem[0]
                nd = elem[1]
                heapq.heappush(h,[nt,nd])
    dists.append(dist[1:])
    
answer = 0
for i in range(n):
    if dists[i][x]+dists[x][i] > answer:
        answer = dists[i][x] + dists[x][i]
        
print(answer)