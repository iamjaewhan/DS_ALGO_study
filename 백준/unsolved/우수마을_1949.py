from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
populations = [0] + list(map(int, input().split()))
loads = defaultdict(set)

for _ in range(n-1):
    v1, v2 = map(int, input().split())
    loads[v1].add(v2)
    loads[v2].add(v1)
    
print(loads)
    