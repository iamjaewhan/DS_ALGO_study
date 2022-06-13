from sys import stdin

input = stdin.readline 
lines = []
n = int(input())
dp = [1]*n

for _ in range(n):
    lines.append(list(map(int, input().split())))
    
lines.sort()

for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(n-max(dp))