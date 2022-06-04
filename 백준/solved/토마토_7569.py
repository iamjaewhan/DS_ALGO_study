from sys import stdin
from collections import deque

input = stdin.readline 
m, n, h = map(int, input().split())
gp = []
q = deque([])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for z in range(h):
    temp = []
    for y in range(n):
        row = list(map(int, input().split()))
        for x in range(m):
            if row[x] == 1:
                q.append([x, y, z])
        temp.append(row)
    gp.append(temp)
    
while q:
    cx, cy, cz = q.popleft()
    
    for i in range(6):
        nx = cx + dx[i]
        ny = cy + dy[i]
        nz = cz + dz[i]

        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and gp[nz][ny][nx] == 0:
            q.append([nx, ny, nz])
            gp[nz][ny][nx] = gp[cz][cy][cx] + 1
            
answer = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if gp[z][y][x] == 0:
                print(-1)
                exit()
            answer = max(answer, gp[z][y][x])
print(answer - 1)