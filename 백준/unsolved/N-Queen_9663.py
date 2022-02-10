num=int(input())

row = [0]*num
answer=0

def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[i]-row[x])==abs(i-x):
            return False
    return True

def findpath(x):
    global answer

    if x==num:
        answer+=1

    else:
        for i in range(num):
            row[x]=i
            if is_promising(x):
                findpath(x+1)

findpath(0)
print(answer)
    
