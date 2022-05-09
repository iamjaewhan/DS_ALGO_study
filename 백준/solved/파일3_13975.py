from sys import stdin
from heapq import heapify, heappop, heappush

input = stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    h = list(map(int, input().split()))
    heapify(h)
    answer = 0
    
    while h:
        n1 = heappop(h)
        try:
            n2 = heappop(h)
            answer += (n1 + n2)
            heappush(h, n1 + n2)
        except IndexError:
            break
    print(answer)
    
    



