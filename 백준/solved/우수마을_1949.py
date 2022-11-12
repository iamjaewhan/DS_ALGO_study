import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
popul = [0] + list(map(int, input().split()))
loads = defaultdict(set)
visited = [False]*(N+1)

dp = [[0, popul[i]] for i in range(N+1)]

for i in range(N-1):
    v1, v2 = map(int, input().split())
    loads[v1].add(v2)
    loads[v2].add(v1)
    
    
def dfs(crnt):
    visited[crnt] = True
    for pre in loads[crnt]:
        if not visited[pre]:
            dfs(pre)
            dp[crnt][1] += dp[pre][0]
            dp[crnt][0] += max(dp[pre][0], dp[pre][1]) 


dfs(1)
print(max(dp[1]))


