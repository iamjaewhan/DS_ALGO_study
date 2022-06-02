from sys import stdin

input = stdin.readline 

T = int(input())
for t in range(T):
    N, M, W = map(int, input().split())
    roads = []
    for m in range(M):
        st, ds, dist = map(int, input().split())
        roads.append((st, ds, dist))
    for w in range(W):
        st, ds, dist = map(int, input().split())
        roads.append((st, ds, -dist))
        
    for i in range(1,N+1):
        dists = [float('inf')]*(N+1)
        dists[i] = 0
        for j in range(N+1):
            for st, ds, dist in roads:
                dists[ds] = min(dists[st] + dist, dists[ds])
        print(dists)

        
            
        
    
    