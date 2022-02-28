from sys import stdin

input = stdin.readline


y,x = map(int, input().split())
gp = [list(map(int, input().split())) for _ in range(y)]
visited = [[0]*x for _ in range(y)]

q = set()
c = set()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def out(gp):
    for row in gp:
        print(row)


def melt(c_list):
    global gp
    while c_list:
        rx,ry = c_list.pop()
        gp[ry][rx] = 0

def bfs(cx,cy):
    global c
    q.add((cx,cy))
    
    while q:
        px,py = q.pop()
        visited[py][px] = 1 

        
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < x and 0 <= ny < y and visited[ny][nx] == 0:
                if gp[ny][nx] == 0:
                    q.add((nx,ny))
                else:
                    c.add((nx,ny))
                    
                    

answer = 0
count = 0

bfs(0,0)
while c:
    visited = [[0]*x for _ in range(y)]
    answer = len(c)
    melt(c)
    count +=1
    bfs(0,0)

print(count)
print(answer)

