from sys import stdin

input = stdin.readline 
n,m = map(int, input().split())
gp = [[] for _ in range(n+1)]

for i in range(m):
    s, t = map(int, input().split())
    gp[t].append(s)
    