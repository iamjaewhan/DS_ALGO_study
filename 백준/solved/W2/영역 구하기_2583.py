from sys import stdin
import sys
from collections import deque

sys.setrecursionlimit(10**3)
input=stdin.readline

m,n,k=map(int, input().split())

board=[[False for x in range(n)] for y in range(m)]


for _ in range(k):
    lx,ly,rx,ry=map(int,input().split())
    for y in range(ly,ry):
        for x in range(lx,rx):
            board[y][x]=True
            
answer=[]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

for y in range(m):
    for x in range(n):
        if board[y][x]==False:
            count=1
            q=deque([])
            q.append([x,y])
            board[y][x]=True
            
            while q:
                cx,cy=q.popleft()

                

                for i in range(4):
                    nx=cx+dx[i]
                    ny=cy+dy[i]

                    if 0<=nx<n and 0<=ny<m and board[ny][nx]==False:
                        q.append([nx,ny])
                        board[ny][nx]=True
                        count+=1


            answer.append(count)
                    
        


print(len(answer))
for num in sorted(answer):
    print(num,end=' ')
    
