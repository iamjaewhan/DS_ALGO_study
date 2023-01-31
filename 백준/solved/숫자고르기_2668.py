import sys

input = sys.stdin.readline

N = int(input())
numbers = dict()
default = 0
for i in range(1, N+1):
    numbers[i] = int(input())

answer = set()

def dfs(crnt, nxt, start, path):
    if nxt in path:
        if nxt == start:
            return path
        else:
            return None
        
    path.add(nxt)
    return dfs(nxt, numbers[nxt], start, path)
    
for i in range(1, N+1):
    cycle = dfs(i, numbers[i], i, set([i]))
    if cycle:
        answer = answer.union(dfs(i, numbers[i], i, set([i])))

print(len(answer))    
for i in answer:
    print(i)