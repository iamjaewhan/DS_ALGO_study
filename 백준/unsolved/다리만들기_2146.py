from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
gp = []
visited = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def out(gp):
    for r in gp:
        print(r)

for _ in range(n):
    gp.append(list(map(int, input().split())))


def bfs_v(x, y):
    temp = [(x, y, 0)]
    q = deque([(x, y)])
    visited[y][x] = count
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n  and visited[ny][nx] == 0 and gp[ny][nx] == gp[cy][cx] :
                visited[ny][nx] = count
                q.append((nx, ny))
                temp.append((nx, ny, 0))
    return temp


count = 1
islands = []
for y in range(n):
    for x in range(n):
         if visited[y][x] == 0 and gp[y][x] != 0:
             islands.append(bfs_v(x, y))
             count += 1

