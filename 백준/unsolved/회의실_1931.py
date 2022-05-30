from sys import stdin

input = stdin.readline 
n = int(input())
meetings = []
for _ in range(n):
    st,ed = map(int, input().split())
    meetings.append((st,ed))
    
meetings.sort(key = lambda x:(-x[1], -x[0]))
dp = [0]*(meetings[0][1]+1)


for i in range(len(dp)):
    if i == meetings[-1][1]:
        m = meetings.pop()
        if m[0] == m[1]:
            dp[i] = dp[m[0]]+1
        else:
            dp[i] = max(dp[m[1]-1], dp[m[0]]+1)
print(dp[-1])
