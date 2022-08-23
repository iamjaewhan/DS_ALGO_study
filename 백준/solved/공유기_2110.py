from sys import stdin

input = stdin.readline

n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

st, ed = 1, houses[-1] - houses[0]
answer = 0

if c == 2:
    print(houses[-1] - houses[0])
else:
    while st < ed:
        mid = (st+ed)//2
        crnt = houses[0]
        count = 1

        for i in houses[1:]:
            if i - crnt >= mid:
                crnt = i
                count += 1

        if count >= c:
            answer = mid
            st = mid +1
        else:
            ed = mid
                    
    print(answer)    