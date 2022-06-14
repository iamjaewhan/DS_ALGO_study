import sys

input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))
answer = 0

for i in range(N):
    count = 0
    last = None
    for j in range(i+1):
        if j != 0:
            inclin = (buildings[i]-buildings[i-j])/(j)
            if last == None or last > inclin:
                count += 1
                last = inclin
        
    last = None
    for j in range(N-(i+1)+1):
        if j != 0:
            inclin = (buildings[i+j]-buildings[i])/(j)
            if last == None or last < inclin:
                count += 1
                last = inclin
    
    answer = max(answer, count)
print(answer)