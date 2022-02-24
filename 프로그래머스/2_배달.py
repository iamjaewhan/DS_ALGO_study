import heapq

def solution(N, road, K):
    INF = float('inf')
    dist = [INF for _ in range(N+1)]
    dist[1] = 0
    
    links = [[] for _ in range(N+1)]
    
    
    for elem in road:
        s,e,w = elem
        links[s].append([w,e])
        links[e].append([w,s])

    h = links[1]
    heapq.heapify(h)
    
    while h:
        elem = heapq.heappop(h)
        w, e = elem
        
        if dist[e] > w:
            dist[e] = w
            adjs = links[e]
            for nd, ne in adjs:
                heapq.heappush(h,[nd+w,ne])
            
    answer = 0    
    for i in range(1,N+1):
        if dist[i] <= K:
            answer += 1
            
    return answer
        
        
        
    
    
    
    
