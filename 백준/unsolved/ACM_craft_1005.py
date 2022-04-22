from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())


for t in range(T):
    N,K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    dp = [0]*(N+1)
    link = [[] for _ in range(N+1)]
    cnt_link = [0]*(N+1)
    
    for k in range(K):
        s,e = map(int, input().split())
        link[s].append(e)
        cnt_link[e] += 1
        
    dest = int(input())
        
    q = deque([])
    start = 0
    for st in range(1,N+1):
        if cnt_link[st] == 0:
            q.append(st)
            dp[st] = D[st]
            

    
    while q:
        crnt = q.popleft()
        
        for toNode in link[crnt]:
            cnt_link[toNode] -= 1
            dp[toNode] = max(dp[toNode],dp[crnt]+D[toNode])
            if cnt_link[toNode] == 0:
                q.append(toNode)
        
        
    

    print("answer : ", dp[dest])
            