from sys import stdin
from collections import defaultdict
import heapq

input = stdin.readline

n = int(input())
m = int(input())

visited = [False]*(n+1)
dist = [float('inf')]*(n+1)
dist[0]=0
buses = defaultdict(list)
routes = [[i] for i in range(n+1)]
routes[0] = []


for _ in range(m):
    c1, c2, w = map(int, input().split())
    buses[c1].append((w, c1, c2))

st, end = map(int, input().split())

h = [(0, 0, st)]

while h:
    w, c1, c2 = heapq.heappop(h)
    if not visited[c2]:
        visited[c2] = True
        routes[c2] = routes[c1]+routes[c2]
        dist[c2] = w
        for route in buses[c2]:
            heapq.heappush(h, (route[0]+dist[c2], route[1], route[2]))
            
print(dist[end])
print(len(routes[end]))
print(*routes[end])
            
