from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
gp = []
gp_n = []
visited = [[0]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    gp.append(list(map(int, input().split())))
    gp_n.append(list(map(int,input().split())))
    
def out(gp):
    for row in gp:
        print(row)
        
def bfs1(x,y,num):
    q = deque([x,y])
    
    while q:
        nx,ny = q.popleft()
        visited[ny][nx] = 1
        gp[ny][nx] = num
        for i in range(4):
            if 0 <= nx+dx[i] < n and 0 <= ny+dy[i] < n and visited[ny+dy[i]][nx+dx[i]] == 0 and  gp[ny+dy[i]][nx+dx[i]] == 1:
                q.append([nx+dx[i],ny+dy[i]])
        
cnt = 1
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0 and gp[y][x] == 1:
            bfs1(x, y, cnt)
            cnt += 1
out(gp)    
out(visited)
        

for i in range(1,cnt+1):
    q = deque([])
    c = [[0]*n for _ in range(n)] 
    for y in range(n):
        for x in range(n):
            if gp_n[y][x] == 1 and gp[y][x] == i:
                q.append([x,y])
                c[y][x] = 1
        
        res = bfs2(i)
        ans = min(ans,res)
print(ans)
                
    
def bfs2(num):
    while q:
        cx,cy = q.popleft()
        
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if gp_n[ny][nx] == 1 and gp[ny][nx] != num:
                    return c[cy][cx]-1
                if gp_n[ny][nx] == 0 and c[ny][nx] == 0:
                    c[ny][nx] = c[cy][cx]+1
                    q.append([nx,ny])
  
    


