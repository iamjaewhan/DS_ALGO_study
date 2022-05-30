a_odd = int(input())/100
b_odd = int(input())/100

non_prime = [0,4,6,8,9,10,12,14,15,16,18]

def nCr(n, r):
    de = 1
    nu = 1
    for i in range(n-r):
        de = de*(n-i)
    for j in range(1, n-r+1):
        nu = nu*j
    return int(de/nu)    
        

dp = [[0]*19 for _ in range(2)]

for i in range(19):
    dp[0][i] = "%0.9f"%float(nCr(18, i)*(a_odd**i)*((1-a_odd)**(18-i)))
    dp[1][i] = "%0.9f"%float(nCr(18, i)*(b_odd**i)*((1-b_odd)**(18-i)))
    

na, nb = 0,0
for num in non_prime:
    na += float(dp[0][num])
    nb += float(dp[1][num])

non = float('%0.9f'%(na*nb))
print(1-non)

