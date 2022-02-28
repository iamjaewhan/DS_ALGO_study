from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

INF = float('inf')
gp = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    gp[i][i] = 0
    

for _ in range(m):
    sn, dn, w = map(int, input().split())
    if gp[sn][dn] > w:
        gp[sn][dn] = w
        

for v in range(1,n+1):
    for s in range(1,n+1):
        for d in range(1,n+1):
            if gp[s][d] > gp[s][v] + gp[v][d]:
                gp[s][d] = gp[s][v] + gp[v][d]
                
for y in range(1,n+1):
    for x in range(1,n+1):
        if gp[y][x] == INF:
            print(0, end=' ')
            continue
        print(gp[y][x], end=' ') 
    print()