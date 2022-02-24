from sys import stdin

input = stdin.readline


n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]



def dfs(grid, visited, loc, n, clr):
    if grid[loc[1]][loc[0]] == clr and visited[loc[1]][loc[0]] == 0:
        visited[loc[1]][loc[0]] = 1
        
        if loc[0]-1 >= 0:
            dfs(grid, visited, [loc[0]-1,loc[1]], n, clr)
        if loc[0]+1 < n:
            dfs(grid, visited, [loc[0]+1,loc[1]], n, clr)
        if loc[1]-1 >= 0:
            dfs(grid, visited, [loc[0],loc[1]-1], n, clr)
        if loc[1]+1 < n:
            dfs(grid, visited, [loc[0],loc[1]+1], n, clr)

        return 1
        
    return 0

answer1 = 0

visited =[[0 for c in range(n)] for r in range(n)]
for r in range(n):
    for c in range(n):
        answer1 += dfs(grid, visited, [c,r], n, grid[r][c])


visited =[[0 for c in range(n)] for r in range(n)] 

answer2 = 0
for i in range(n):
    for ind, val in enumerate(grid[i]):
        if val == "G":
            grid[i][ind] = "R"

for r in range(n):
    for c in range(n):
        answer2 += dfs(grid, visited, [c,r], n, grid[r][c])
        
print(answer1)
print(answer2)