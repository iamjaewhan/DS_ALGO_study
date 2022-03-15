from sys import stdin
import sys
sys.setrecursionlimit(10**8)

input = stdin.readline

row, col = map(int, input().split())
gp = []
visited = [[-1]*col for _ in range(row)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(row):
    gp.append(list(map(int, input().split())))
    
def dfs(sx,sy):
    if sx == col-1 and sy == row-1:
        return 1
    
    if visited[sy][sx] != -1:
        return visited[sy][sx]
    
    cnt = 0
    
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < col and 0 <= ny < row and gp[ny][nx] < gp[sy][sx]:
            cnt += dfs(nx,ny)
    
    visited[sy][sx] = cnt
    
    return visited[sy][sx]

print(dfs(0, 0))

    

    
    