n = int(input())
gd = [[" "]*(n+1) for _ in range(n+1)]

    
def out():
    for i in range(1, n+1):
        print("".join(gd[i][1:]))    
        
def star(sx, sy, ex, ey):
    d = (ex+1-sx)//3
    if d == 0:
        gd[sy][sx] = "*"
    
    else:
        for r in range(3):
            for c in range(3):
                if r != 1 or c != 1:
                    star(sx+d*c , sy+d*r, sx+d*(c+1)-1, sy+d*(r+1)-1)
                        
star(1,1,n,n)

out()