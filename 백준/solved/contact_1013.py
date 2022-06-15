from sys import stdin
import re

input = stdin.readline

T = int(input())
p = re.compile('(100+1+|01)+')

for t in range(T):
    sign = input().replace('\n', '')
    if p.fullmatch(sign):
        print("YES")
    else:
        print("NO")
    