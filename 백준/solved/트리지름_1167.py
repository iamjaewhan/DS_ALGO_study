from sys import stdin
from collections import defaultdict, deque
import heapq

v = int(input())
routes = defaultdict(list)

for _ in range(1, v+1):
    nums = list(map(int, input().split()))
    i = nums[0]
    nums = nums[1:-1]
    for j in range(0, len(nums), 2):
        routes[i].append((nums[j], nums[j+1]))

        
def get_dist(start):
    visited = [False]*(v+1)
    visited[start] = True
    q = deque([(start, 0)])
    max_ind = start
    max_dist = 0
    
    while q:
        crnt, cdist = q.popleft()
        
        if cdist > max_dist:
            max_ind = crnt
            max_dist = cdist
            
        for nxt, ndist in routes[crnt]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, ndist+cdist))
        
    return (max_dist, max_ind)
        
max_dist, nxt_start = get_dist(1)
max_dist, end_index = get_dist(nxt_start)

print(max_dist)

    
    