
n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))


mat = [[0]*100 for r in range(n+1)]

for y in range(1,n+1):
    for x in range(1,100):
        if x-L[y-1] >= 0:
            mat[y][x] = max(mat[y-1][x], mat[y-1][x-L[y-1]]+J[y-1])
        else:
            mat[y][x] = mat[y-1][x]
print(mat[-1][-1])