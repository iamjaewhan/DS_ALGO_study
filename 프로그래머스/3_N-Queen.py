#N-Queen
def dfs(seq,n,row):
    count=0
    if row==n:
        return 1


    for col in range(n):
        seq[row]=col
        for ind in range(row):
            if abs(seq[row]-seq[ind])==abs(row-ind):
                break
            if seq[ind]==seq[row]:
                break
        else:
            count+=dfs(seq,n,row+1)
    return count
            
    

def solution(n):
    seq=[0]*n
    return dfs(seq,n,0)

    
