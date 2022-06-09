from sys import stdin

input = stdin.readline
dx = [0,1,0,-1] #순서대로 북,동,남,서
dy = [-1,0,1,0]

n,m = map(int, input().split())
r,c,d = map(int, input().split())
gp = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
answer = 1

def out(gp):
    for r in gp:
        print(r)
        
def dfs(x, y, d, visited, gp):
    visited[y][x] = 1
    for i in range(1,5):
        
        nx = x+dx[(d-i)%4]
        ny = y+dy[(d-i)%4]
        if 0 <= nx < m and 0 <= ny < n:
            if visited[ny][nx] == 0 and gp[ny][nx] == 0:
                global answer
                answer += 1
                return dfs(nx, ny, (d-i)%4 , visited, gp)
    if gp[y+dy[d-2]][x+dx[d-2]] == 0:
        return dfs(x+dx[d-2], y+dy[d-2], d, visited, gp)
    
    
dfs(c, r, d, visited, gp)
print(answer)

