#게임 맵 최단거

def solution(maps):
    col = len(maps[0])
    row = len(maps)
    
    #(x,y)
    q = []
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    graph = [[-1 for _ in range(col)] for _ in range(row)]
    
    graph[0][0] = 1
    q.append((0,0))
    
    while q:
        x,y = q.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<col and 0<=ny<row and maps[ny][nx] == 1 and graph[ny][nx] == -1:
                graph[ny][nx] = graph[y][x]+1
                q.append((nx,ny))
                
    return graph[-1][-1]

"""
def solution(maps):
    col, row = len(maps), len(maps[0])
    q = []
    q.append((0,0,1))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False for c in range(col)] for r in range(row)]
    visited[0][0] = True
    
    while q:
        x,y,step = q.pop(0)
        
        if x == row-1 and y == col-1:
            return step
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < col and 0<= ny < row and maps[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append((nx, ny, step+1))
                
    return -1
    
"""
            
            
            
    
    
    
    
    
