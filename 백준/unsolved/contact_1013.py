from sys import stdin
import re

input = stdin.readline

T = int(input())

for t in range(T):
    strin = input().split('01')
    for substr in strin:
        if re.match(r"^(100+1|01)+$", substr):
            continue
        else:
            print("NO")
            break
    print("YES")