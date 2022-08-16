import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
gp = []
visited = [0]*n 

for _ in range():
    gp.append(list(map(int, input().split())))
    
plan = list(map(int, input().split()))
q = deque([0])

print(gp)
print(visited)

# while q:
#     last = q.popleft()
#     visited[last] = 1
    
#     for i in range(n):
#         if visited[i] == 0 and gp[last][i] == 1:
#             visited[i] = 1
#             q.append(i)
         
         
   
answer = "YES"

for i in plan:
    if visited[i-1] == 0:
        answer = "NO"
        break
    
print(answer)

