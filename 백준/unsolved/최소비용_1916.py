from sys import stdin


input = stdin.readline

N = int(input())
M = int(input())
lines = [[] for _ in range(N+1)]


for _ in range(M):
    sp,ep,w = map(int,input().split())
    

heap = []

def djk(start):
    
