from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

N, M = map(int, input().split())
gp = [input() for _ in range(N)]
# 벽 부수지 않은 경우, 벽을 부순 경우
dist = [[[1000001, 1000001] for _ in range(M)] for _ in range(N)]

def solve():
    q = deque([(0, 0, 1)])
    dist[0][0][0] = 1
    
    while q:
        cx, cy, ld = q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                
                # 다음 칸이 1인 경우
                if gp[ny][nx] == '1' and ld > 0:
                    if dist[ny][nx][1] > dist[cy][cx][0] + 1:
                        q.append((nx, ny, ld-1))
                        dist[ny][nx][1] = dist[cy][cx][0] + 1
                
                # 다음 칸이 0인 경우
                if gp[ny][nx] == '0':
                    
                    if ld > 0 and dist[ny][nx][0] > dist[cy][cx][0] + 1:
                        dist[ny][nx][0] = dist[cy][cx][0] + 1
                        q.append((nx, ny, ld))
            
                    elif ld == 0 and dist[ny][nx][1] > dist[cy][cx][1] + 1:
                        dist[ny][nx][1] = dist[cy][cx][1] + 1
                        q.append((nx, ny, ld))
                        
    answer = min(dist[-1][-1])

    if answer > 1000000:
        return -1
    return answer
                    

print(solve())

