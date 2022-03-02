from sys import stdin

input = stdin.readline

n,k = map(int, input().split())
crc = []
for _ in range(n):
    crc.append(int(input()))
    
sorted(crc)
gp = [0]*(k+1)
gp[0] = 1

for c in crc:
    for x in range(1,k+1):
        if x-c >= 0:
            gp[x] += gp[x-c]

print(gp[-1])

