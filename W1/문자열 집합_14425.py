from sys import stdin

n,m=map(int,stdin.readline().split())

word_set=set()

for i in range(n):
    word_set.add(stdin.readline())

count=0

for j in range(m):
    if stdin.readline() in word_set:
        count+=1

print(count)

