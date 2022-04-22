
import sys

input= sys.stdin.readline

n = int(input())

gp = [[0]*(n+1) for _ in range(n+1)]
points = [[0]*(n+1) for _ in range(n+1)]

while 1:
    n1,n2 = map(int, input().split())
    if n1 == -1 and n2 == -1:
        break
    gp[n1][n2] = 1
    gp[n2][n1] = 1
    
for via in range(1,n+1):
    for y in range(1,n+1):
        for x in range(1,n+1):
            if gp[y][x] == 0 and gp[y][via]*gp[via][x]!=0 and y != x != via:
                gp[y][x] = gp[y][via]+gp[via][x]
              
answer = float('inf') 
candi = []
for i in range(1,len(gp)):
    if max(gp[i]) < answer:
        answer = max(gp[i])
        candi = [i]
    elif max(gp[i]) == answer:
        candi.append(i)

print(answer, len(candi))
print(" ".join(map(str,candi)))
                