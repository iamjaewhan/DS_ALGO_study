import sys

input = sys.stdin.readline
n, h = map(int, input().split())
gp = [0]*(h)

for i in range(n):
    height = int(input())
    if i%2 == 0:
        gp[0] += 1
        gp[height] -= 1
    else:
        gp[h-height] += 1

for i in range(h-1):
    gp[i+1] += gp[i]
    
print(min(gp), gp.count(min(gp)))