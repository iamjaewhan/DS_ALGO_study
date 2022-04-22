from sys import stdin
import heapq

INF = float('inf')
input = stdin.readline

n,m,x = map(int, input().split())
h = heapq.heapify([])
gp = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,t = map(int, input().split())
    gp[s].append([t,e])
    
def djik(st, ed):
    dist = [INF]*(n+1)
    dist[st] = 0
    h = []
    for elem in  gp[st]:
        heapq.heappush(h,elem)
    
    while h:
        t, e = heapq.heappop(h)
        if t < dist[e]:
            dist[e] = t
            if e == ed:
                return dist[ed]
            for nt,ne in gp[e]:
                heapq.heappush(h,[nt+dist[e], ne])
    return dist[ed]

total_tdist = [INF]*(n+1)
total_tdist[x] = 0
for i in range(1,n+1):
    if i !=x :
        i_tdist = djik(i, x) + djik(x, i)
        if total_tdist[i] > i_tdist:
            total_tdist[i] = i_tdist
            

print(max(total_tdist[1:]))
    
        
        
    
    