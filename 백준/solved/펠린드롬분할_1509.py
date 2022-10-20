string = list(input())
N = len(string)

dp1 = [[0]*N for _ in range(N)]
dp2 = [float('inf')]*(N+1)
dp2[-1]=0

for i in range(N):
    dp1[i][i] = 1

for i in range(1, N):
    if string[i] == string[i-1]:
        dp1[i][i-1] = 1
        dp1[i-1][i] = 1

for l in range(2, N):
    for i in range(l, N):
        if string[i-l] == string[i] and dp1[i-1][i-l+1] == 1:
            dp1[i][i-l] = 1
            dp1[i-l][i] = 1
            
for e in range(N):
    for s in range(e+1):
        if dp1[s][e] == 1:
            dp2[e] = min(dp2[s-1]+1, dp2[e])
        else:
            dp2[e] = min(dp2[e], dp2[e-1]+1)

print(dp2[N-1])



