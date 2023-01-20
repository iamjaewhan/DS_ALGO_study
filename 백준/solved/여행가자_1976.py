import sys
from collections import deque

input = sys.stdin.readline

def custom_int(str):
    return int(str)-1

N = int(input())
M = int(input())
gp = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(custom_int, input().split()))
answer = "YES"


def get_adj(node):
    adjs = []
    
    for i in range(N):
        if gp[node][i] != 0 and node != i:
            adjs.append(i)
    
    return adjs


def get_connected(start):
    connected = set()
    connected.add(start)
    q = deque([start])
    
    while q:
        crnt = q.popleft()
        
        for nxt in get_adj(crnt):
            if nxt not in connected:
                connected.add(nxt)
                q.append(nxt)
                
    return connected

connected_cities = get_connected(plan[0])

for city in plan:
    if city not in connected_cities:
        answer = "NO"
        break
    
print(answer)