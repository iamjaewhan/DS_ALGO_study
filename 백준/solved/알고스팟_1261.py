from sys import stdin
import heapq

#출력 메소드
def out(graph):
    for row in graph:
        print(row)

input = stdin.readline
x,y = map(int, input().split())

graph = []

for i in range(y):
    graph.append(list(map(int,list(input())[:-1])))
    
visited = [[0]*(x) for _ in range(y)]
    
#dist,x,y
h = [[0,0,0]]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while h:
    dist,nx,ny = heapq.heappop(h)
    if visited[ny][nx] == 0:
        graph[ny][nx] = dist
        visited[ny][nx] = 1

        for i in range(4):
            if 0 <= nx+dx[i] < x and 0 <= ny+dy[i] < y and visited[ny+dy[i]][nx+dx[i]] == 0:
                print("x,y = ",nx+dx[i],ny+dy[i] )
                heapq.heappush(h, [graph[ny+dy[i]][nx+dx[i]]+dist,nx+dx[i],ny+dy[i]])
    
    
    

out(visited)
print()
out(graph)



