str1 = input()
str2 = input()

gp = [[""]*(len(str1)+1) for _ in range(len(str2)+1)]

    
for y in range(1, len(str2)+1):
    for x in range(1, len(str1)+1):
        if str2[y-1] == str1[x-1]:
            gp[y][x] = gp[y-1][x-1] + str2[y-1]
        else:
            if len(gp[y-1][x]) > len(gp[y][x-1]):
                gp[y][x] = gp[y-1][x]
            else:
                gp[y][x] = gp[y][x-1]

print(len(gp[-1][-1]))
if gp[-1][-1]:
    print(gp[-1][-1])