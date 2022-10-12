import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
gd = []
#상,우,하,좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


for i in range(n):
    st = input().strip()
    
    if 'B' in st:
        b_loc = [st.index('B'), i]
        st = st.replace('B', '.')
    if 'R' in st:
        r_loc = [st.index('R'), i]
        st = st.replace('R', '.')
    gd.append(st)


def out():
    for r in gd:
        print(r)

def move(r_loc, b_loc, direction):
    if direction == 0:
        if r_loc[1] < b_loc[1]:
            nr_loc, nb_loc = _move(r_loc, b_loc, direction)
        else:
            nb_loc, nr_loc = _move(b_loc, r_loc, direction)
        
    elif direction == 1:
        if r_loc[0] > b_loc[0]:
            nr_loc, nb_loc = _move(r_loc, b_loc, direction)
        else:
            nb_loc, nr_loc = _move(b_loc, r_loc, direction)
                  
    elif direction == 2:
        if r_loc[1] >= b_loc[1]:
            nr_loc, nb_loc = _move(r_loc, b_loc, direction)
        else:
            nb_loc, nr_loc = _move(b_loc, r_loc, direction)
                   
    elif direction == 3:
        if r_loc[0] <= b_loc[0]:
            nr_loc, nb_loc = _move(r_loc, b_loc, direction)
        else:
            nb_loc, nr_loc = _move(b_loc, r_loc, direction)
        
    return nr_loc + nb_loc
            
def _move(first_loc, second_loc, direction):
    fx, fy = first_loc
    while gd[fy + dy[direction]][fx + dx[direction]] == '.':
        fx += dx[direction]
        fy += dy[direction]
    if gd[fy + dy[direction]][fx + dx[direction]] == 'O':
        fx += dx[direction]
        fy += dy[direction]
        
    sx, sy = second_loc
    while gd[sy + dy[direction]][sx + dx[direction]] == '.' and (sx+dx[direction] != fx or sy+dy[direction] != fy):
        sx += dx[direction]
        sy += dy[direction]
    if gd[sy + dy[direction]][sx + dx[direction]] == 'O':
        if sx+dx[direction] == fx and sy+dy[direction] == fy:
            return first_loc, second_loc
        else:
            sx += dx[direction]
            sy += dy[direction]
        
    return [[fx,fy],[sx,sy]]
    
    

# elem = (빨간공 위치, 파란공 위치, count)

first_loc = ''
for ch in r_loc+b_loc:
    first_loc += str(ch)
    
q = deque([[first_loc, 10]])
answer = -1
visited = set()

while q:
    loc_str, count = q.popleft()
    l = len(loc_str)//4
    rx, ry, bx, by = int(loc_str[0:l]),int(loc_str[1*l:1*l+l]),int(loc_str[2*l:2*l+l]),int(loc_str[3*l:3*l+l])
    
    if count < 11:
        if gd[ry][rx] == 'O':
            answer = 10 - count
            break
        elif gd[by][bx] == 'O':
            continue
        
        else:
            for i in range(4):
                nrx, nry, nbx, nby = move([rx, ry], [bx, by], i)
                nloc_str = str(nrx) + str(nry) + str(nbx) + str(nby)
                if nloc_str not in visited:
                    visited.add(nloc_str)
                    q.append([nloc_str, count-1])
if answer >= 11:
    answer = -1
    
print(answer)
            
    
