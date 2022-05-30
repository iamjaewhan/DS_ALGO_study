from collections import deque

row,col = map(int, input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

ice = []
for r in range(row):
    ice.append(list(map(int, input().split())))
    

# def getIceberg(ice):
#     icebergs = []
#     for r in range(len(ice)):
#         for c in range(len(ice[r])):
#             if ice[r][c] == 0:
#                 for i in range(4):
#                     nr = r + dy[i]
#                     nc = c + dx[i]
#                     if 0 <= nr < len(ice) and 0 <= nc < len(ice[r]) and ice[nr][nc] > 0:
#                         icebergs.append([nr, nc])
#     return icebergs

# def melts(icebergs):
#     for r,c in icebergs:
#         ice[r][c] = max(0, ice[r][c]-1)


# def getIslands(ice):
#     islands = 0
#     visited = [[0]*col for _ in range(row)]
#     for r in range(row):
#         for c in range(col):
#             if ice[r][c] > 0 and visited[r][c] == 0:
#                 islands += 1
#                 visited[r][c] = 1
#                 q = deque([[r,c]])
#                 while q:
#                     cr, cc = deque.popleft(q)
#                     for i in range(4):
#                         nr = cr + dy[i]
#                         nc = cc + dx[i]
#                         if 0 <= nr < row and 0 <= nc < col and visited[nr][nc] == 0:
#                             visited[nr][nc] = 1
#                             q.append([nr,nc])
#     return islands

# answer = 0
# count = 0
# numOfIcebergs = getIslands(ice)
# while numOfIcebergs == 1:
#     melts(getIceberg(ice))
#     count += 1
#     numOfIcebergs = getIslands(ice)
    
# if numOfIcebergs > 1:
#     print(count)
# elif numOfIcebergs == 0:
#     print(0)

    
                
                
