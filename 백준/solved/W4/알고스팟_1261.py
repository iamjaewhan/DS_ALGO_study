from sys import stdin
import heapq

input=stdin.readline
x,y=map(int, input().split())

mat=[]
for i in range(y):
    mat.append(list(input()))
    
dist=[[0 for c in range(x)] for r in range(y)]
h=[]
heapq.heappush([0,[0,0]])

def search(loc,x,y):
    


