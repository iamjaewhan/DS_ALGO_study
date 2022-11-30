def get_answer(number : int):
    dp = [1]*(number+1)
    
    for i in range(1, number+1):
        dp[i] = dp[i-1]
        if i - 2 >= 0:
            dp[i] += dp[i-2]*2
    print(dp[-1])
    
while True:
    try:
        number = int(input())
        get_answer(number)
    except Exception:
        break  
        