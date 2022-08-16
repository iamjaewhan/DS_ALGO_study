from sys import stdin
from collections import deque

input = stdin.readline

row, col = map(int, input().split())
gp = [input().strip("\n") for _ in range(row)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def get_longest_dist(crnt, visited):
    _max_dist = 0
    crnt_loc = crnt + [_max_dist]
    queue = deque([crnt_loc])
    visited[crnt[1]][crnt[0]] = 1
    while queue:
        cx, cy, cd = queue.popleft()
        _max_dist = max(_max_dist, cd)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < col and 0 <= ny < row and visited[ny][nx] == 0 and gp[ny][nx] == 'L':
                visited[ny][nx] = 1
                queue.append([nx, ny, cd+1])
    return _max_dist
        
max_dist = 0
for y in range(row):
    for x in range(col):
        if gp[y][x] == 'L':
            visited = [[0]*col for _ in range(row)]
            crnt_dist = get_longest_dist([x,y], visited)
            max_dist = max(max_dist, crnt_dist)
print(max_dist)