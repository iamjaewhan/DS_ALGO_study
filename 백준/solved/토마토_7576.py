from sys import stdin
from collections import deque

input = stdin.readline

gp = []
col, row = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque([])

for _ in range(row):
    gp.append(list(map(int, input().split())))
    
def out(gp):
    for row in gp:
        print(row)

for y in range(row):
    for x in range(col):
        if gp[y][x] == 1:
            q.append([x,y])
            
def bfs():
    while q:
        cx,cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
        
            if 0 <= nx < col and 0 <= ny < row:
                if gp[ny][nx] == 0:
                    gp[ny][nx] = gp[cy][cx]+1
                    q.append([nx,ny])
            
bfs()

answer = 1

for r in gp:
    if 0 in r:
        answer = 0
        break
    answer = max(answer, max(r))

print(answer-1)




"""
def getAdj(x,y):
    next_loc = set()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < col and 0 <= ny < row:
            if gp[ny][nx] == 0:
                next_loc.add((nx,ny))
    return next_loc

def ripe(next_loc):
    for nx,ny in next_loc:
        gp[ny][nx] = 1
    
answer = 0
is_done = False

while not is_done:
    next_set = set()
    for y in range(row):
        for x in range(col):
            if gp[y][x] == 1:
                next_set = next_set.union(getAdj(x, y))

    if len(next_set) == 0:
        is_done = True
        break
    ripe(next_set)
    answer += 1

for row in gp:
    if 0 in row:
        answer = -1
print(answer)
"""
    
        