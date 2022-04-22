import sys

input = sys.stdin.readline

N = int(input())
buildings = [0]+list(map(int, input().split()))


def getBuild(ind):
    count = 0
    #오른쪽 위치 건물들 구하기    
    for r in range(1,N+1-ind):
        is_behind = 0
        ang = (buildings[ind+r]-buildings[ind])/r
        for rv in range(r):
            if buildings[ind+rv] >= buildings[ind] + ang*rv:
                is_behind = 1
                break
        count += (1-is_behind)
    
        
    
    #왼쪽 위치 건물 개수 구하기
    for l in range(1,ind-1):
        is_behind = 0
        ang = (buildings[ind-l]-buildings[ind])/l
        for lv in range(l):
            if buildings[ind-lv] >= buildings[ind] + ang*lv:
                is_behind = 1
                break
        count += (1-is_behind)
        
        
    
    
    
    return count
    


answer = 0
for i in range(1,N+1):
    count = getBuild(i)
    if count > answer:
        answer = count
        
print(answer)