import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]

for num in nums:
    if num > dp[-1]:
        dp.append(num)
    else:
        l, r = 0, len(dp)-1
        
        while l <= r:
            mid = (l+r)//2
            if dp[mid] == num:
                l = mid
                break
            elif dp[mid] > num:
                r = mid-1
            else:
                l = mid+1
        dp[l] = num
    
print(len(dp))
            
