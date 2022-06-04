from sys import stdin
input = stdin.readline 

n = int(input())
s = list(map(int, input().split()))

inc_dp = [1]*n
dec_dp = [1]*n

for i in range(1,n):
    for j in range(i+1):
        if s[i] > s[i-j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[i-j]+1)
        if s[n-i-1] > s[n-i-1+j]:
            dec_dp[n-i-1] = max(dec_dp[n-i-1], dec_dp[n-i-1+j]+1)
            
answer = 0
for i in range(n):
    answer = max(answer, inc_dp[i] + dec_dp[i]-1)
print(answer)
        
    