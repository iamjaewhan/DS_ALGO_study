r1,c1,r2,c2 = map(int, input().split())


def getNum(x,y):
    ax, ay = abs(x),abs(y)
    
    if x*y == 0:
        if x + y == 0:
            return 1
        if x > 0:
            return getNum(x-1,y)+8*x-7
        elif x < 0:
            return getNum(x+1, y)+8*ax-3
        elif y > 0:
            return getNum(x, y-1)+8*y-1
        else:
            return getNum(x, y+1)+8*ay-5
    else:
        if x > 0:
            if ay/ax >= 1:
                if y < 0:
                    return getNum(0, y)-x
                return getNum(0, y)+x
            if ay/ax < 1:
                if y > 0:
                    return getNum(x, 0)-ay
                return getNum(x, 0)+ay
        
        else:
            if ay/ax >= 1:
                return getNum(0, y)
            else:
                return getNum(x, 0)

    return 0
            








for y in range(r1, r2+1):
    for x in range(c1, c2+1):
        print(getNum(x, y), end=' ')
    print()
    
