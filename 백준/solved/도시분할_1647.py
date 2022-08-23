from sys import stdin
import heapq

input = stdin.readline

n,m = map(int, input().split())
links = []
visited = [0]*(n+1)
answer = 0

def get_parent(parents, x):
    if parents[x] != x:
        return get_parent(parents, parents[x])
    return x

def union_parents(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    n1, n2, w = map(int, input().split())
    links.append((w, n1, n2))
    
links.sort(reverse=True)

parents = [i for i in range(n+1)]
while links:
    w, n1, n2 = links.pop()
    if get_parent(parents, n1) != get_parent(parents, n2):
        answer += w
        last = w
        union_parents(parents, n1, n2)

print(answer-last)
