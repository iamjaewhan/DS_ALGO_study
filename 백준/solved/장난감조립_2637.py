import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

# index : crnt, (부모 노드, 필요 개수)
connect = [[] for _ in range(n + 1)] 
degree = [0] * (n + 1)

q = deque()
gp = [[0]*(n+1) for _ in range(n+1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    connect[b].append((a, c))
    degree[a] += 1
    
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        
while q:
    crnt = q.popleft()
    for parent, w in connect[crnt]:
        if gp[crnt].count(0) == n+1:
            gp[parent][crnt] = w
        else:
            for i in range(1, n+1):
                gp[parent][i] += gp[crnt][i]*w
        degree[parent] -= 1
        if degree[parent] == 0:
            q.append(parent)

for i in range(1,n+1):
    if gp[n][i] != 0:
        print(i, gp[n][i])


    


#DFS방법
# 완성부품 : {필요부품: 개수}
# parts = defaultdict(dict)
# answer = defaultdict(int)

# for _ in range(m):
#     x, y, k = map(int, input().split())
#     parts[x][y] = k
    
# def dfs(crnt_key, count):
#     for nxt_key in parts[crnt_key].keys():
#         if nxt_key in parts.keys():
#             dfs(nxt_key, count*parts[crnt_key][nxt_key])
#         else:
#             answer[nxt_key] += count*parts[crnt_key][nxt_key]
            
# dfs(n,1)
# for key in sorted(answer.keys()):
#     print(key, answer[key])



