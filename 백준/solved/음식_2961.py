import sys

input = sys.stdin.readline

sour = []
bitter = []

n = int(input())

s_dp = [1]*(1<<n)
b_dp = [0]*(1<<n)

for _ in range(n):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)
    
for i in range(1,len(s_dp)):
    for j in range(n, -1, -1):
        if i >= 1<<j:
            s_dp[i] = s_dp[i-(1<<j)]*sour[j]
            b_dp[i] = b_dp[i-(1<<j)]+bitter[j]
            break
    
answer = float('inf')    
for i in range(1, 1<<n):
    answer = min(answer, abs(s_dp[i]-b_dp[i]))

print(answer)
    
    
    
