
tiles = {0: [5], 1: [4,5], 2: [3,5], 3: [2], 4: [1,5], 5: [0,1,2,4,5]}
    
# def out(dp):
#     for r in dp:
#         print(*r)

def get_answer(n):
    dp = [[0]*6 for _ in range(n+1)]
    dp[0][5] = 1
    
    for i in range(n):
        for j in range(6):
            for k in tiles[j]:
                dp[i+1][k] += dp[i][j]
          
    print(dp[-1][-1])
        
        

T = int(input())
for i in range(T):
    n = int(input())
    get_answer(n)
    