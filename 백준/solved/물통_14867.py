from collections import deque



def get_answer(va, vb, ta, tb):
    visited = {}
    visited[(0,0)] = 0
    q = deque([(0, 0)])
    
    while q:
        cx, cy = q.popleft()
        keys = visited.keys()
        
        if (cx, 0) not in keys:
            visited[(cx,0)] = visited[(cx, cy)] + 1
            q.append((cx, 0))
        
        if (0, cy) not in keys:
            visited[(0, cy)]= visited[(cx, cy)] + 1
            q.append((0, cy))
            
        if (va, cy) not in keys:
            visited[(va, cy)] = visited[(cx, cy)] + 1
            q.append((va, cy))
            
        if (cx, vb) not in keys:
            visited[(cx, vb)] = visited[(cx, cy)] + 1
            q.append((cx, vb))
        
        if cx + cy >= vb and (cx+cy-vb, vb) not in keys:
            visited[(cx+cy-vb, vb)] = visited[(cx, cy)] + 1
            q.append((cx+cy-vb, vb))
        
        if cx + cy < vb and (0, cx+cy) not in keys:
            visited[(0, cx+cy)] = visited[(cx, cy)] + 1
            q.append((0, cx+cy))
        
        if cx + cy >= va and (va, cx+cy-va) not in keys:
            visited[(va, cx+cy-va)] = visited[(cx, cy)] + 1
            q.append((va, cx+cy-va))
        
        if cx + cy < va and (cx+cy, 0) not in keys:
            visited[(cx+cy, 0)] = visited[(cx, cy)] + 1
            q.append((cx+cy, 0))
    
    if (ta, tb) in visited.keys():
        return visited[(ta, tb)]
    return -1
            
    
    
vA, vB, tA, tB = map(int, input().split())
print(get_answer(vA, vB, tA, tB))