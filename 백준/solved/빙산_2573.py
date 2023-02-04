import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

N, M = map(int, input().split())
gp = [list(map(int, input().split())) for _ in range(N)]

def getIceberg(x, y):
    melting = []
    q = deque([(x,y)])
    visited[y][x] = True
    
    while q:
        cx, cy = q.popleft()
        
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False and gp[ny][nx] > 0:
                visited[ny][nx] = True
                q.append((nx, ny))
            
            if 0 <= nx < M and 0 <= ny < N and gp[ny][nx] == 0:
                melting.append((cx, cy))
    return melting
    

        
count = 0
answer = 0

while True:
    visited = [[False]*M for _ in range(N)]
    icebergs = []
    
    for y in range(N):
        for x in range(M):
            if visited[y][x] is False and gp[y][x] > 0:
                icebergs.append(getIceberg(x, y))

    
    if len(icebergs) > 1:
        answer = count
        break
    elif len(icebergs) == 0:
        break
    else:
        for tx, ty in icebergs[0]:
            if gp[ty][tx] > 0:
                gp[ty][tx] -= 1 
        count += 1

print(answer)
