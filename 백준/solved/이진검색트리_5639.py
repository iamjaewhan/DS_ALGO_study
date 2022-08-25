from sys import stdin, setrecursionlimit

setrecursionlimit(10**9)
input = stdin.readline

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break
    
def binary(l, r):
    if l > r:
        return
    
    temp = r + 1
    
    for i in range(l+1, r+1):
        if nums[i] > nums[l]:
            temp = i
            break
    
    binary(l+1, temp-1)
    binary(temp,r)
    print(nums[l])
    
    
            
    
binary(0, len(nums)-1)
    
    