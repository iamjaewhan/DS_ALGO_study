from sys import stdin

input = stdin.readline

v, e = map(int, input().split())
gp = [[float('inf')]*v for _ in range(v)]


for _ in range(e):
    v1, v2 , dist = map(int, input().split())
    gp[v1-1][v2-1] = dist


for via in range(v):
    for v1 in range(v):
        for v2 in range(v):
            if gp[v1][via] + gp[via][v2] < gp[v1][v2]:
                gp[v1][v2] = gp[v1][via] + gp[via][v2]

cycles = [gp[i][i] for i in range(v)]
answer = min(cycles)
print(-1) if answer == float('inf') else print(answer)