s, n, k, r1, r2, c1, c2 = map(int, input().split())

def out(m):
    for r in m:
        print(r)

mat = [[0]*(n**s) for _ in range(n**s)]

out(mat)