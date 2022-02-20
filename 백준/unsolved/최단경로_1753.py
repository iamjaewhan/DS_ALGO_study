from sys import stdin
import heapq

input=stdin.readline

n,e = map(int, input().split())
st = int(input())
INF = float('inf')
heap=[]
linkes=[[] for _ in range(n+1)]
dist=[INF] * (n+1)

def djk(start):
    dist[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        w,n = heapq.heappop(heap)

        if w > dist[n]:
            continue

        for wei, next_n in linkes[n]:
            next_wei = w + wei

            if next_wei < dist[next_n]:
                heapq.heappush(heap, (next_wei,next_n))


for _ in range(e):
    s, d, w = map(int,input().split())
    linkes[s].append((w,d))


djk(st)

for i in range(1,n+1):
    if dist[i] == INF:
        print("INF")
        continue
    print(dist[i])
