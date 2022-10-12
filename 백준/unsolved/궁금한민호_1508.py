from sys import stdin

input = stdin.readline

n = int(input())
def out(gp):
    for row in gp:
        print(row)

gp = [list(map(int, input().split())) for _ in range(n)]
gp2 = [[1]*n for _ in range(n)]
gp3 = [[0]*n for _ in range(n)]
answer = 0

for st in range(n):
    for ed in range(n):
        for via in range(n):
            if st != via and ed != via and st != ed:
                if gp[st][ed] == gp[st][via] + gp[via][ed]:
                    gp2[st][ed] = 0
                    gp3[st][via] = gp[st][via]
                    gp3[via][st] = gp[st][via]
                    gp3[ed][via] = gp[via][ed]
                    gp3[via][ed] = gp[via][ed]
                    
                elif gp[st][ed] > gp[st][via] + gp[via][ed]:
                    answer = -1

out(gp)
print()


if answer != -1:
    for y in range(n):
        for x in range(y, n):
            if gp2[y][x] > 0:
                # gp2[y][x] = gp[y][x]
                answer += gp[y][x]

out(gp2)
print(answer)
out(gp3)
    

