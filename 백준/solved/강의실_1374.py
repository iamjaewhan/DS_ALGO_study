from sys import stdin
import heapq

input = stdin.readline 

n = int(input())
room =[] 
heapq.heapify(room)
lec = []
heapq.heapify(lec)

for _ in range(n):
    i, s, e = map(int, input().split())
    heapq.heappush(lec, (s, e))
    
while lec:
    s, e = heapq.heappop(lec)
    if len(room):
        if room[0] <= s:
            heapq.heappop(room)
            heapq.heappush(room, e)
        else:
            heapq.heappush(room, e)
    else:
        heapq.heappush(room, e)

print(len(room))    
