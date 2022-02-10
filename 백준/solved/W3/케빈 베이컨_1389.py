from sys import stdin

input=stdin.readline

v,e=map(int,input().split())


matrix=[[float('inf')]*(v+1) for j in range(v+1)]

for _ in range(v+1):
    matrix[_][_]=0

for _ in range(e):
    n1,n2=map(int,input().split())
    matrix[n1][n2]=1
    matrix[n2][n1]=1

for via in range(1,v+1):
    for start in range(1,v+1):
        for dest in range(1,v+1):
            if matrix[start][dest]>matrix[start][via]+matrix[via][dest]:
                matrix[start][dest]=matrix[start][via]+matrix[via][dest]

line=1
total=sum(matrix[line][1:])
for row in range(1,v+1):
    if sum(matrix[row][1:])<total:
        line=row
        total=sum(matrix[line][1:])

    


print(line)
