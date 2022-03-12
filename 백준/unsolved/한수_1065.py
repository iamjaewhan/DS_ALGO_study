n = int(input())

def check(list):
    is_han = 1
    if len(list) == 1:
        return is_han
    
    for i in range(0,len(list)-2):
        if list[i]-list[i+1] != list[i+1]-list[i]+2:
            is_han = 0
            return is_han
    return is_han
    
def out(num_list):
    n = len(num_list)
    answer = 0
    for i in range(0,n):
        answer += num_list[i]*(10**(n-i))
    return(answer)  

for i in range(n,-1,-1):
    num_list = list(map(int,str(i)))
    if check(num_list):
        print(out(num_list))
        