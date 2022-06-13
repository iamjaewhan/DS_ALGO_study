from sys import stdin

input = stdin.readline 

T = int(input())
for _ in range(T):
    answer = "NO"
    n, m, w = map(int, input().split())
    dist = [2147483647]*(n+1)
    dist[1]= 0
    adjList = [[] for _ in range(n+1)]
    
    for _ in range(m):
        s, e, d = map(int, input().split())
        adjList[s].append((d,e))
        adjList[e].append((d,s))
    for _ in range(w):
        s, e, d = map(int, input().split())
        adjList[s].append((-d,e))
        
    for i in range(1,n+1):
        for j in range(1, n+1):
            for w, dn in adjList[j]:
                if dist[dn] > w + dist[j]:
                    dist[dn] = w + dist[j]
                    if i == n:
                        answer = "YES"

    print(answer)
            
        
    
    