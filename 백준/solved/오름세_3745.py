import sys

input = sys.stdin.readline

    
def LISS(n,nums):
    dp = [nums[0]]
    
    for num in nums:
        if num > dp[-1]:
            dp.append(num)
        else:
            l,r = 0, len(dp)-1
            
            while l < r:
                mid = (l+r)//2
                
                if dp[mid] == num:
                    l = mid
                    break
                elif dp[mid] < num:
                    l = mid+1
                else:
                    r = mid
            dp[l] = num
    print(len(dp))
    
    
while True:
    try:
        n = int(input())
        if not n:
            break
        nums = list(map(int, input().split()))
        LISS(n, nums)
    except Exception as e:
        break