from collections import deque

row,col = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

ice = []
for r in range(row):
    ice.append(list(map(int, input().split())))
    
#빙산의 영역을 구하는 bfs
def bfs(x,y):
    q.append([x,y])
    while q:
        cx,cy = q.popleft()
        visited[cy][cx] = 1
        
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0 <= nx < col and 0 <= ny < row:
                if ice[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([nx,ny])
                elif ice[ny][nx] == 0:
                    counts[cy][cx] += 1
                
    return 



q = deque([])
count = 0
while True:
    visited = [[0]*col for _ in range(row)]
    counts = [[0]*col for _ in range(row)]
    islands = 0
    
    for y in range(row):
        for x in range(col):
            if ice[y][x] != 0 and visited[y][x] == 0:
                islands += bfs(x, y)
                
    
    for y in range(row):
        for x in range(col):
            ice[y][x] -= counts[y][x]
            if ice[y][x] < 0:
                ice[y][x] = 0
                
    if islands > 1:
        count = 0
        break
    if islands == 0:
        break
    
    
    count += 1
    
            
print(count)
                
                
    