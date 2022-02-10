import sys
from sys import stdin

n=int(input())
sys.setrecursionlimit(10**6)


linked_node=[[]for i in range(n+1)]

for i in range(n-1):
    nd1,nd2=map(int,stdin.readline().split())
    linked_node[nd1].append(nd2)
    linked_node[nd2].append(nd1)

parent_num=[None for i in range(n+1)]



def formTree(p_node,parent_num,linked_node):
    for num in linked_node[p_node]:
        if parent_num[num]==None:
            parent_num[num]=p_node
            formTree(num,parent_num,linked_node)
    

formTree(1,parent_num,linked_node)

for i in range(2,n+1):
    print(parent_num[i])
