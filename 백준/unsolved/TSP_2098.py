import sys

input = sys.stdin.readline

n = int(input())
W = []

for _ in range(n):
    W.append(list(map(int, input().split())))
    
def out(gp):
    for row in gp:
        print(row)
        
