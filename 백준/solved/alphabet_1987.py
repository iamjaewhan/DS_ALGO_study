import sys
from collections import deque

input = sys.stdin.readline 

r, c = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
gp = []
answer = 1

for _ in range(r):
    gp.append(list(input()))
    
def bfs(x,y):
    s = set(gp[y][x])
    global answer
    q = deque([(x,y, gp[y][x])])
    while q:
        cx, cy, st = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and gp[ny][nx] not in st:
                q.append((nx, ny, st + gp[ny][nx]))
                answer = max(answer, len(st)+1)
        
bfs(0,0)
print(answer)


# def dfs(s, x, y):
#     global answer
#     s.add(gp[y][x])
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < c and 0 <= ny < r and gp[ny][nx] not in s:
#             dfs(s, nx, ny)
#     answer = max(answer, len(s))
#     s.remove(gp[y][x])
    
# trace = set()
# dfs(trace, 0, 0)
# print(answer)
    

