import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def flip_row(crnt_int, row):
    if row == 1:
        bit_str = "111000000"
    elif row == 2:
        bit_str = "111000"
    else:
        bit_str = "111"
    return int(bin(crnt_int),2)^int(bit_str,2)

def flip_col(crnt_int, col):
    if col == 1:
        bit_str = "100100100"
    elif col == 2:
        bit_str = "010010010"
    else:
        bit_str = "001001001"
    return int(bin(crnt_int),2)^int(bit_str,2)

def flip_diag(crnt_int, dir):
    if dir == 1:
        bit_str = "100010001"
    else:
        bit_str = "001010100"
    return int(bin(crnt_int),2)^int(bit_str,2)

for t in range(T):
    crnt = ''
    for _ in range(3):
        crnt += ''.join(input().split())
    crnt = crnt.replace('T','0').replace('H','1')   
    
    dp = [-1]*((1<<9))
    q = deque()
    q.append(int(crnt,2))
    dp[int(crnt,2)] = 0
    answer = -1
    while q:
        elem = q.popleft()
        if elem == 0 or elem == (1<<9)-1:
            answer = dp[elem]
            break
        else:
            for i in range(1,4):
                nxt = flip_col(elem, i)
                if dp[nxt] == -1:
                    q.append(nxt)
                    dp[nxt] = dp[elem]+1
                nxt = flip_row(elem, i)
                if dp[nxt] == -1:
                    q.append(nxt)
                    dp[nxt] = dp[elem]+1
            for i in range(1,3):
                nxt = flip_diag(elem, i)
                if dp[nxt] == -1:
                    q.append(nxt)
                    dp[nxt] = dp[elem]+1
    print(answer)
    
                
                    
    

    
    
    
    
    

    
    
    
    

    
    