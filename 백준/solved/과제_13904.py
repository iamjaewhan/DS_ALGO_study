from sys import stdin
import heapq

input = stdin.readline 

n = int(input())
assignments = []
for _ in range(n):
    assignments.append(list(map(int, input().split())))
    
assignments.sort(key=lambda x:(x[0], x[1]))
last_day = assignments[-1][0]
h = []

answer = 0
for i in range(last_day, 0, -1):
    while assignments and i <= assignments[-1][0]:
        deadline, w = assignments.pop()
        heapq.heappush(h, [-w, deadline])

    while h:
        candi = heapq.heappop(h)
        if candi[1] >= i:
            answer += (-1)*candi[0]
            break
    
    
        
print(answer)

    