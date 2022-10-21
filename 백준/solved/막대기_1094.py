x = int(input())
length = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(length)):
    if x >= length[i]:
        count += 1
        x -= length[i]
    
    if x == 0:
        break
print(count)