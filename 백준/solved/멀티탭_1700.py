import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

counts = defaultdict(int)
indexes = defaultdict(lambda: deque())

for i in range(K):
    counts[nums[i]] += 1
    indexes[nums[i]].append(i)


    
count = 0
plugs = set()

for i in nums:
    if len(plugs) < N or i in plugs:
        plugs.add(i)
    
    else:
        count += 1
        done = False
        
        if not done:
            for k in plugs:
                if counts[k] == 0:
                    plugs.remove(k)
                    plugs.add(i)
                    done = True
                    break
        
        if not done:
            max_ind = -1
            max_key = -1
            
            for k in plugs:
                if max_ind < indexes[k][0]:
                    max_key = k
                    max_ind = indexes[k][0]
            
            plugs.remove(max_key)
            plugs.add(i)        
                    
    counts[i] -= 1
    indexes[i].popleft()

    
print(count)
        
    