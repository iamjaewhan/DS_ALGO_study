from sys import stdin

input = stdin.readline 

n,l = map(int, input().split())
gp = []
for _ in range(n):
    gp.append(list(map(int, input().split())))

answer = 0
gp2 = [[0]*n for _ in range(n)]

for y in range(n):
    is_p = 1
    for x in range(1,n):
        if not is_p:
            break
        if gp[y][x] == gp[y][x-1]:
            continue
        elif gp[y][x] == gp[y][x-1]-1:
            for i in range(l):
                if x+i >= n or gp[y][x] != gp[y][x+i] or gp2[y][x+i] == 1:
                    is_p = 0
                    break
            if is_p:
                for i in range(l):
                    gp2[y][x+i] = 1
                    
        elif gp[y][x] == gp[y][x-1]+1:
            for i in range(l):
                if x-1-i < 0 or gp[y][x-1] != gp[y][x-i-1] or gp2[y][x-1-i] == 1:
                    is_p = 0
                    break
            if is_p:
                for i in range(l):
                    gp2[y][x-1-i] = 1
        else:
            is_p = 0
            break
    if is_p:
        answer += 1
gp2 = [[0]*n for _ in range(n)]

for x in range(n):
    is_p = 1
    for y in range(1,n):
        if not is_p:
            break
        if gp[y][x] == gp[y-1][x]:
            continue
        elif gp[y][x] == gp[y-1][x]-1:
            for i in range(l):
                if y+i >= n or gp[y][x] != gp[y+i][x] or gp2[y+i][x] == 1:
                    is_p = 0
                    break
            if is_p:
                for i in range(l):
                    gp2[y+i][x] = 1
        elif gp[y][x] == gp[y-1][x]+1:
            for i in range(l):
                if y-1-i < 0 or gp[y-1-i][x] != gp[y-1][x] or gp2[y-1-i][x] == 1:
                    is_p = 0
                    break
            if is_p:
                for i in range(l):
                    gp2[y-1-i][x] = 1
        else:
            is_p = 0
            break
    if is_p:
        answer += 1
        
print(answer)