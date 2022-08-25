from sys import stdin
from collections import deque, defaultdict

input = stdin.readline

n, m = map(int, input().split())
gp = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_border(gp):
    visited = [[0]*m for _ in range(n)]
    q = deque([(0,0)])
    visited[0][0] = 1
    borders = defaultdict(int)
    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 0 and gp[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
                elif gp[ny][nx] == 1:
                    borders['c%dr%d'%(nx,ny)] += 1
    return get_loc(list(filter(lambda x:borders[x] >= 2,borders.keys())))
                    
def get_loc(loc_list):
    locs = []
    for loc in loc_list:
        loc = loc.strip('c')
        locs.append(tuple(map(int, loc.split('r'))))
    return locs

def melt(borders):
    for x,y in borders:
        gp[y][x] = 0
    

count = 0
borders = get_border(gp)
while borders:
    count += 1
    melt(borders)
    borders = get_border(gp)
print(count)    