import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, list(input())[:-1])) for _ in range(n)]
answer = 0

for y in range(1, n):
    for x in range(1, m):
        if matrix[y][x] == 1:
            matrix[y][x] = max(matrix[y][x], min(matrix[y-1][x], matrix[y-1][x-1], matrix[y][x-1])+1)

for r in matrix:
    answer = max(answer, max(r))

print(answer*answer)
            
            