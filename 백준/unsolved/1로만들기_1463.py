n = int(input())

gp = [[0]*(4) for row in range(n+1)]


for y in range(1,n+1):
    for x in range(1,4):
        if x == 1:
            gp[y][x] = y-1
        
        if x == 2:
            if y % 2 == 0:
                gp[y][x] = gp[y//2][x]+1
            else:
                gp[y][x] = min(gp[y][x-1],gp[y-1][x]+1)
            
        if x == 3:
            if y % 3 == 0:
                if y % 2 == 0:
                    gp[y][x] = min(gp[y][x-1], gp[y//3][x]+1)
                else:
                    gp[y][x] = gp[y//3][x]+1
            elif y % 3 == 1:
                gp[y][x] = min(gp[y][x-1],gp[y-1][x]+1)
            else:
                gp[y][x] = min(gp[y][x-1], gp[y-2][x]+2)
    

print(gp[n][3])

"""
40
정답: 5 (40 20 10 9 3 1)
출력: 6 (40 39 13 12 4 2 1)

41
정답: 6 (41 40 20 10 9 3 1)
출력: 7 (41 40 39 13 12 4 2 1)

52
정답: 6 (52 26 13 12 4 2 1)
출력: 52 (52 51 17 16 8 4 2 1)

76
정답: 6 (76 38 19 18 6 2 1)
출력: 7 (76 75 25 24 8 4 2 1)

80
정답: 6 (80 40 20 10 9 3 1)
출력: 7 (80 40 39 13 12 4 2 1)
    """