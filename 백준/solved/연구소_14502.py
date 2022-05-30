from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline 

def out(m):
    for r in m:
        print(r)
        
        
rows, cols = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(rows)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def bfs():
    global answer
    m = deepcopy(mat)
    q = deque([])
    for r in range(rows):
        for c in range(cols):
            if m[r][c] == 2:
                q.append([r,c])
    
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r+dy[i]
            nc = c+dx[i]
            if 0 <= nr < rows and 0 <= nc < cols and m[nr][nc] == 0:
                m[nr][nc] = 2
                q.append([nr,nc])
    temp = 0
    for row in m:
        temp += row.count(0)
    
    answer = max(answer, temp)
                
def buildWall(built_num):
    if built_num == 3:
        bfs()
        return
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                mat[r][c] = 1
                buildWall(built_num + 1)
                mat[r][c] = 0
        
buildWall(0)
print(answer)


