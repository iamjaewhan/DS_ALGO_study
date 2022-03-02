from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
INF = float('inf')

gp = [[INF]*n for _ in range(n)]
for i in range(n):
    gp[i][i] = 0

def out(gp):
    for row in gp:
        count = 0
        for col in row:
            if col == INF:
                count += 1
        print(count)

for _ in range(m):
    w, l = map(int, input().split())
    gp[w-1][l-1] = 1
    gp[l-1][w-1] = -1
    

    
for v in range(n):
    for y in range(n):
        for x in range(n):
            if gp[y][v] == gp[v][x] and gp[y][v] != (0 or INF):
                gp[y][x] = gp[y][v]
                
out(gp)