from sys import stdin

input = stdin.readline 

n = int(input())
poles = list(map(int, input().split()))

answer = n
sub = [poles[0]]

def binarySearch(st , ed, tg):
    while st < ed:
        mid = (st + ed)//2
        if sub[mid] < tg:
            st = mid + 1
        else:
            ed = mid
    sub[st] = tg

for i in range(1,n):
    if poles[i] > sub[-1]:
        sub.append(poles[i])
    else:
        binarySearch(0, len(sub)-1, poles[i])
        
print(n-len(sub))