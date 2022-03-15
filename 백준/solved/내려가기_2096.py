from sys import stdin

input = stdin.readline

n = int(input())

max_dp = [0]*3
min_dp = [0]*3

tmax_dp = [0]*3
tmin_dp = [0]*3

for _ in range(n):
    a,b,c = map(int, input().split())

    for i in range(3):
        if i == 0:
            max_dp[i] = max(tmax_dp[i],tmax_dp[i]) + a
            min_dp[i] = min(tmin_dp[i],tmin_dp[i]) + a
        elif i == 1:
            max_dp[i] = max(tmax_dp[i],tmax_dp[i+1],tmax_dp[i-1]) + b
            min_dp[i] = min(tmin_dp[i],tmin_dp[i+1],tmin_dp[i-1]) + b
        else:
            max_dp[i] = max(tmax_dp[i],tmax_dp[i-1]) + c
            min_dp[i] = min(tmin_dp[i],tmin_dp[i-1]) + c
    
    tmax_dp = max_dp.copy()
    tmin_dp = min_dp.copy()
    
print(max(max_dp), min(min_dp))