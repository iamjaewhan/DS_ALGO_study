from sys import stdin

n = int(input())
nums = list(map(int, input().split()))

dp = []

for i in range(n):
    if len(dp) == 0 or dp[-1] < nums[i]:
        dp.append(nums[i])
        
    else:
        l, r = 0, len(dp)-1
        
        while l < r:
            mid = (l+r)//2

            if dp[mid] > nums[i]:
                r = mid
            elif dp[mid] < nums[i]:
                l = mid+1
            else:
                l = mid
                break
        dp[l] = nums[i]
        
print(len(dp))
        