from sys import stdin
from heapq import heappop, heappush, heapify

input = stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    count += 1
    
    gp = [list(map(int, input().split())) for _ in range(n)]
    dist_gp = [[float('INF')]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    
    h = [(gp[0][0], 0, 0)]
    visited[0][0] = 1
    heapify(h)
    
    while h:
        dist, cx, cy = heappop(h)
        dist_gp[cy][cx] = dist
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and dist_gp[ny][nx] > gp[ny][nx]+dist:
                visited[ny][nx] = 1
                heappush(h, [gp[ny][nx]+dist, nx, ny])
        
    
    print("Problem %d: %d"%(count, dist_gp[n-1][n-1]))