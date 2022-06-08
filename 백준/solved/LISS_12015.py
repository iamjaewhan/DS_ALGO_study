from sys import stdin

input = stdin.readline 

n = int(input())
s = list(map(int, input().split()))
dp = []

for i in range(n):
    if len(dp) == 0 or dp[-1] < s[i]:
        dp.append(s[i])
    else:
        l,r = 0, len(dp)-1
        
        while l < r:
            if dp[(l+r)//2] < s[i]:
                l = (l+r)//2+1
            elif dp[(l+r)//2] > s[i]:
                r = (l+r)//2
            else:
                l = (l+r)//2
                break
        dp[l] = s[i]

print(len(dp))           
        


