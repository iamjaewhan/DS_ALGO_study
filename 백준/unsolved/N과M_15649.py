n,m = map(int, input().split())

nums = list(range(1,n+1))
print(nums)

def getS(ls, count):
    if count > 0:
        for elem in ls:
            temp = ls
            print(elem, end=' ')
            getS(temp.remove(elem), count-1)
    print()
            
getS(nums, m)
        