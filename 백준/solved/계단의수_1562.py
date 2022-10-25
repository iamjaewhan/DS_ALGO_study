n = int(input())
MAX = (1<<10)-1

def out(dp):
    for r in dp:
        print(r)
        
        
dp = [[0]*(MAX+1) for _ in range(10)]

for i in range(1,10):
    dp[i][1<<i] = 1
    
for _ in range(2, n+1):
    next_dp = [[0]*(MAX+1) for _ in range(10)]
    
    for i in range(10):
        for j in range(MAX+1):
            if i > 0:
                next_dp[i][j|(1<<i)] = (next_dp[i][j|(1<<i)]+dp[i-1][j])%1000000000
            if i < 9:
                next_dp[i][j|(1<<i)] = (next_dp[i][j|(1<<i)]+dp[i+1][j])%1000000000
                
    dp = next_dp
    
print(sum(dp[i][MAX] for i in range(10))%1000000000)






""" 첫번째 풀이 - 메모리 초과
n = int(input())

answer = set()

def get_step(crnt, left):
    if left == 0:
        if '0' in crnt and '9' in crnt:
            answer.add(crnt)
    else:
        last = int(crnt[-1])
        plus = last + 1
        minus = last - 1
        if plus<10:
            get_step(crnt+str(plus), left-1)
        if minus >= 0:
            get_step(crnt+str(minus), left-1)

            
            
for i in range(1,10):
    get_step(str(i), n-1)
    
print(len(answer))
            
"""