n = int(input())
nums = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(dp)
ind = max(dp)
print(ind)
subseq = []
for i in range(n-1, -1, -1):
    if dp[i] == ind:
        subseq.append(nums[i])
        ind -= 1
subseq.reverse()  
print(*subseq)