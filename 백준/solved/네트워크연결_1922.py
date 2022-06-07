from sys import stdin
import heapq

input = stdin.readline 

n = int(input())
m = int(input())
gp = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    n1, n2, cost = map(int, input().split())
    gp[n1].append((cost, n2))
    gp[n2].append((cost, n1))

visited[1] = 1
h = []
for elem in gp[1]:
    heapq.heappush(h, elem)
    
answer = 0
while h:
    cost, nxt = heapq.heappop(h)
    if visited[nxt] == 0:
        answer += cost
        visited[nxt] = 1
        for elem in gp[nxt]:
            if visited[elem[1]] == 0:
                heapq.heappush(h, elem)

print(answer)
            

    