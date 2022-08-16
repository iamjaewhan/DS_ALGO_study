from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
gp = []
dist_sum = 0
size = 2
crnt = []
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for i in range(n):
    gp.append(list(map(int, input().split())))
    crnt = [gp[-1].index(9), len(gp)-1] if 9 in gp[-1] else crnt

def bfs(ct, gp, visited, size):
    crnt = ct + [0]
    q = deque([crnt])
    visited[ct[1]][ct[0]] = 1
    while q:
        cx, cy, cdist = q.popleft()
        
        if gp[cy][cx] != 0 and gp[cy][cx] != 9 and gp[cy][cx] < size:
            return cdist,[cx,cy]
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and gp[ny][nx] < size:
                visited[ny][nx] = 1
                q.append([nx, ny, cdist+1])
    return None, None

def get_answer(gp, crnt):
    answer = 0
    crnt_size = 2
    growing_size = 2
    while True:
        visited = [[0]*n for _ in range(n)]
        dist, nxt_loc = bfs(crnt, gp, visited, int(growing_size))
        if dist:
            answer += dist
            gp[crnt[1]][crnt[0]] = 0
            growing_size += 1/crnt_size
            crnt_size = int(growing_size)
            crnt = nxt_loc
            gp[crnt[1]][crnt[0]] = 9
        else:
            break
    return answer


print(get_answer(gp, crnt))



    

    


