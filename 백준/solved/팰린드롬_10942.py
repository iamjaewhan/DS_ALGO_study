from sys import stdin

input = stdin.readline
n = int(input())
string = list(map(int, input().split()))
m = int(input())

dp = [[0]*n for _ in range(n)]
    
for gap in range(n):
    for l in range(n-gap):
        r = l + gap
        
        if l == r:
            dp[l][r] = 1
        
        elif string[l] == string[r]:
            if l+1 == r:
                dp[l][r] = 1
            else:
                dp[l][r] = dp[l+1][r-1]*1


for i in range(m):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])