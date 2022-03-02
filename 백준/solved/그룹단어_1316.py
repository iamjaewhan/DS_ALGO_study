from sys import stdin


input = stdin.readline

n = int(input())

def check(str):
    ap = ""
    for ch in str:
        if ch in ap and ap[-1] != ch:
            return 0
        ap += ch
    return 1


answer = 0
for i in range(n):
    answer += check(input())
    
print(answer)