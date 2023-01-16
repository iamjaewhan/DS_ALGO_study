from collections import deque
import sys

input = sys.stdin.readline


dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
N, L, R = map(int, input().split())
gp = []

for _ in range(N):
    gp.append(list(map(int, input().split())))


def get_unions(x, y):
    unions = set([(x, y)])
    visited[y][x] = True
    q = deque([(x, y)])
    
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:

                if visited[ny][nx] == False and L <= abs(gp[ny][nx]-gp[cy][cx]) <= R:
                    visited[ny][nx] = True
                    unions.add((nx, ny))
                    q.append((nx, ny))
    
    return unions
    

def move(union):
    total_sum = 0
    
    for x,y in union:
        total_sum += gp[y][x]
        
    avg = total_sum//len(union)
    
    for x,y in union:
        gp[y][x] = avg
        

answer = 0

while True:
    unions = []
    visited = [[False]*N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                union = get_unions(x, y)
                if len(union) > 1:
                    unions.append(union)
            
    if not unions:
        break
    
    answer += 1
    
    
    for union in unions:
        move(union)    

print(answer)
            
            