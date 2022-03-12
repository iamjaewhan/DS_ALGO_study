import itertools

n = int(input())
a = itertools.permutations(range(1,n+1),n)

for row in a:
    row = list(row)
    for elem in row:
        print(elem, end = ' ')
    print()