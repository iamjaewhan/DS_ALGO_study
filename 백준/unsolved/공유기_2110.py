from sys import stdin

input = stdin.readline

n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

st, ed = 1, houses[-1] - houses[0]
answer = 0

if c == 2:
    print(ed - st)
else:
    while st <= ed:
        mid = (st+ed)//2
        count = 1
        crnt = houses[0]
        for i in houses:
            if i - crnt >= mid:
                count += 1
                crnt = i
        if count >= c:
            answer = mid
            st = mid + 1
        elif count < c:
            ed = mid - 1
    print(answer)    