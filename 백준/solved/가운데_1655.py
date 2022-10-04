from sys import stdin
import heapq

input = stdin.readline
max_h = [] # 최대힙 : 중간값보다 작은 요소들 저장
min_h = [] # 최소힙 : 중간값보다 큰 요소들 저장
heapq.heapify(max_h)
heapq.heapify(min_h)

def get_answer(n):
    if len(max_h) == 0:
        heapq.heappush(max_h, (-1)*n)
    
    else:
        if (-1)*max_h[0] < n:
            if len(max_h) == len(min_h):
                heapq.heappush(min_h, n)
                small = heapq.heappop(min_h)
                heapq.heappush(max_h, (-1)*small)
            elif len(max_h) == len(min_h)+1:
                heapq.heappush(min_h, n)
        else:
            if len(max_h) == len(min_h):
                heapq.heappush(max_h, (-1)*n)
            elif len(max_h) == len(min_h)+1:
                heapq.heappush(max_h, (-1)*n)
                big = heapq.heappop(max_h)
                heapq.heappush(min_h, (-1)*big)
    print((-1)*max_h[0])
    


for _ in range(int(input())):
    num = int(input())
    get_answer(num)
    
    
    
    