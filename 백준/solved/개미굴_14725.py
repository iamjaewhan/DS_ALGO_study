import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

tree = dict()

def addTree(tree, elems):
    for elem in elems:
        if elem in tree:
            tree = tree[elem]
        else:
            tree[elem] = dict()
            tree = tree[elem]

for i in range(n):
    input_list = input().split()
    m, route = int(input_list[0]), input_list[1:]
    addTree(tree, route)
    

def printTree(tree, depth):
    for key in sorted(tree.keys()):
        print("--"*depth+"%s"%key)
        printTree(tree[key], depth+1)
        
        
printTree(tree,0)
            
        
    
    