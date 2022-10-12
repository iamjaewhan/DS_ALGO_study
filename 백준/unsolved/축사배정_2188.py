import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n, m = map(int, input().split())
rooms = [-1]*(m+1)
cows = defaultdict(list)

for i in range(1, n+1):
    cows[i] = list(map(int, input().split()))[1:]
    

def assign(cow):
    for i in cows[cow]:
        if visited[i] == 1:
            continue
        visited[i] = 1
        if rooms[i] == -1 or assign(rooms[i]):
            rooms[i] = cow
            return True
        return False   
        
answer = 0
    
for i in range(1, n+1):
    visited = [0]*(m+1)
    if assign(i):
        answer += 1
    print(rooms)

        
print(answer)

