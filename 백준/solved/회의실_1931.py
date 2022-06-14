from sys import stdin
import heapq

input = stdin.readline 
n = int(input())
answer = 0
meetings = []
heapq.heapify(meetings)
for _ in range(n):
    st,ed = map(int, input().split())
    heapq.heappush(meetings, (ed,st))
    
last = 0
while meetings:
    meeting = heapq.heappop(meetings)
    if meeting[1] >= last:
        answer += 1
        last = meeting[0]
        
print(answer)
    

    
