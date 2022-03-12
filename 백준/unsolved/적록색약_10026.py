from sys import stdin
import heapq

input = stdin.readline


n = int(input())
gp = [list(input().rstrip()) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[0]*(n) for _ in range(n)]

def bfs(loc):
    q = [loc]
    
    while h:
        x,y = q.pop(0)
        clr = gp[y][x]

        visited[y][x] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and gp[ny][nx] == clr:
                q.append([nx,ny])

answer1 = 0
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            bfs([x,y])
            answer1 += 1
            
            

    
    
visited = [[0]*(n) for _ in range(n)]

for y in range(n):
    for x in range(n):
        if gp[y][x] == "G":
            gp[y][x] = "R"
        
answer2 = 0
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            bfs([x,y])
            answer2 += 1
                
print(answer1, answer2)
        
    
    
    














"""
def dfs(gp, loc):
    x,y = loc
    clr = gp[y][x]
    visited[y][x] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[ny][nx] == 0 and  gp[ny][nx] == clr:
                dfs(gp,[nx,ny])
            
                

answer1 = 0
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            dfs(gp,[x,y])
            answer+=1
        
visited = [[0]*(n) for _ in range(n)]

for y in range(n):
    for x in range(n):
        if gp[y][x] == "G":
            gp[y][x] = "R"
      
answer2 = 0      
for y in range(n):
    for x in range(n):
        if visited[y][x] == 0:
            dfs(gp,[x,y])
            answer2 +=1
            

        
print(answer1, answer2)
"""

