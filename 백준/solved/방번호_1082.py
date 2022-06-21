import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
m = int(input())

pd = dict()
for i in range(len(p)):
    pd[p[i]] = str(i)
    
dp = ['-1']*(m+1)
dp[0] = ""

for i in range(1, m+1):
    temp = []
    for k in pd.keys():
        if i-k >= 0 and dp[i-k] != '-1':
            temp.append(
                int(''.join(sorted(dp[i-k]+pd[k], reverse=True)))
                        )
    if temp:
        dp[i] = str(max(temp))
        
dp = list(map(int, dp[1:]))
print(max(dp))