import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [100001]*100001

dp[N] = 0
h = [(dp[N], N)]

heapq.heapify(h)
answer = 100001

while h:
    count += 1
    crnt_dist, crnt_node = heapq.heappop(h)
    
    if crnt_node == K:
        answer = crnt_dist
        break
    
    if 0 <= crnt_node - 1 <= 100000:
        if dp[crnt_node-1] > crnt_dist+1:
            dp[crnt_node-1] = crnt_dist + 1
            heapq.heappush(h, (crnt_dist+1, crnt_node-1))
        
    if 0 <= crnt_node + 1 <= 100000:
        if dp[crnt_node+1] > crnt_dist+1:
            dp[crnt_node+1] = crnt_dist + 1
            heapq.heappush(h, (crnt_dist+1, crnt_node+1))
            
    if 0 <= 2*crnt_node <= 100000:
        if dp[2*crnt_node] > crnt_dist:
            dp[2*crnt_node] = crnt_dist
            heapq.heappush(h, (crnt_dist, 2*crnt_node))
    
print(answer)