import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
nodes = defaultdict(list)
nodes_heading = list(map(int, input().split()))
for i in range(N):
    nodes[nodes_heading[i]].append(i)
deleted_node = int(input())
answer = 0

def get_leaves(node):
    count = 0
    
    if node in nodes.keys():
        for child in nodes[node]:
            if child != deleted_node:
                count += get_leaves(child)
    if count == 0:
        count += 1

    return count

start = nodes[-1][0]
answer = get_leaves(start)
if start == deleted_node:
    answer = 0
    
print(answer)