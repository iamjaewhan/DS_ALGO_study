import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []
heapq.heapify(h)

for _ in range(n):
    v = int(input())
    heapq.heappush(h, v)
    
answer = 0
while len(h) > 1:
    n1, n2 = heapq.heappop(h), heapq.heappop(h)
    answer += (n1+n2)
    heapq.heappush(h, n1+n2)
    
print(answer)