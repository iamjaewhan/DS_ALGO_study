import sys

dx = [1, -1, 0]
dy = [0, 0, 1]

input = sys.stdin.readline

r, c = map(int, input().split())
gd = [input() for _ in range(r)]
visited = [[0]*c for _ in range(r)]


def out():
    for r in gd:
        print(r)
        
        
def dfs(crnt):
    cx, cy = crnt
    
    for i in range(3):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
                

