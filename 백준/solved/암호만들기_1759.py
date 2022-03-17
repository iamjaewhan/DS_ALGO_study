from sys import stdin
from itertools import permutations, combinations

l,c = map(int, input().split())
chrs = input().split()
chrs.sort()

vowels = set('aeiou')

com = list(combinations(chrs, l))

for i in com:
    c = set(i)-vowels
    if 2 <= len(c) and l-len(c) >= 1:
        print("".join(i))