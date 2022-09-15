from sys import stdin
import heapq

input = stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

lectures.sort(reverse=True)
h = []
heapq.heapify(h)

while lectures:
    lec = lectures.pop()
    if not h:
        heapq.heappush(h, lec[1])
    else:
        earliest = heapq.heappop(h)
        if earliest > lec[0]:
            heapq.heappush(h, earliest)
            heapq.heappush(h, lec[1])
        else:
            heapq.heappush(h, lec[1])

print(len(h))