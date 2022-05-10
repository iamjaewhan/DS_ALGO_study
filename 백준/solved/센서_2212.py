from sys import stdin

input = stdin.readline

N = int(input())
K = int(input())
sensor_loc = list(map(int, input().split()))

if K >= N:
    print(0)
else:
    dist = []
    sensor_loc.sort()
    for i in range(1, N):
        dist.append(sensor_loc[i] - sensor_loc[i-1])
    
    dist.sort()
    for _ in range(K-1):
        dist.pop()
        
    print(sum(dist))