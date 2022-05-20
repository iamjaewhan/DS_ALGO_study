n = int(input())
inf = float('inf')

dp = [0]*(n+1)
h = [0,1] #육각수의 개수 : 인덱스, 점의 개수 : 요소

while h[-1] < n:
    h.append((len(h)-1)*4+1+h[-1])


for i in range(1,n+1):
    min_val = dp[i-1]
    for j in range(1,len(h)):
        if h[j] > i:
            break
        min_val = min(min_val, dp[i - h[j]])
    dp[i] = min_val + 1
    
        
        
print(dp[-1])