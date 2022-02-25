import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    currency = list(map(int, input().split()))
    M = int(input())
    
    #그래프 초기화
    graph = [[0]*(M+1) for _ in range(len(currency)+1)]
    for row in graph:
        row[0] = 1
    
    
    for y in range(1,len(currency)+1):
        for x in range(1, M+1):
            if x - currency[y-1] >= 0:
                graph[y][x] = graph[y-1][x] + graph[y][x-currency[y-1]]
            else:
                graph[y][x] = graph[y-1][x]

    print(graph[-1][-1])    
    
    
    