str1 = input()
str2 = input()
dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for y in range(1, len(str2)+1):
    for x in range(1, len(str1)+1):
        if str1[x-1] == str2[y-1]:
            dp[y][x] = dp[y-1][x-1]+1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
            
print(dp[-1][-1])