from sys import stdin
from collections import deque
import re

input = stdin.readline

T = int(input())

def out(num_list):
    print("[", end = '')
    for i in range(len(num_list)):
        if i == (len(num_list) - 1):
            print(num_list[i], end='')
        else:
            print(num_list[i] + ",", end="")
    print("]")

for i in range(T):
    side = 0
    operation = re.findall(r'[A-Z]', input())
    n = int(input())
    nums = list(re.findall(r"[0-9]+", input()))
    nums = deque(nums)
    
    try:
        for op in operation:
            if op == "R":
                side = (side+1) % 2
            else:
                if side == 1:
                    nums.pop()
                else:
                    nums.popleft()
    except IndexError:
        print("error")
        continue
    
    if side == 0:
        out(list(nums))
    else:
        out(list(nums)[::-1])

    