import sys


input = sys.stdin.readline
n, k = map(int, input().split())
coins = set([int(input()) for _ in range(n)])

dp = [10001]*(k+1)
dp[0] = 0

for i in range(1, k+1):
    for coin in coins:
        if i-coin >= 0:
            dp[i] = min(dp[i-coin]+1, dp[i])
            
print(dp[i]) if dp[i] < 10001 else print(-1)