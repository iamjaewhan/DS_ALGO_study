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
    count = 1
    while st <= ed:
        mid = (st+ed)//2
        
        crnt = houses[0]
        for i in houses[1:]:
            if i - crnt >= mid:
                crnt = i
                count += 1

        if count >= c:
            answer = mid
            st = mid
        else:
            ed = mid-1
                    
    print(answer)    