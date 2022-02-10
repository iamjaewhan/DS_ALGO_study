def getS(x,n,m,arr,s):
    s.append(x)
    if len(s)==m:
        print(s)
    else:
        unvisited=list(filter(lambda x:arr[x]==0, range(len(arr))))
        for i in unvisited:
            getS(i,n,m,arr,s)
            
            




n,m=map(int,input().split())
arr=[0]*n
s=[]

getS(0,n,m,arr,s)
            
        
