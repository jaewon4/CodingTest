import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

n = input().split('-')
num = []

for i in n:
    s = i.split('+')
    sum = 0
    for j in s:
        sum += int(j)
    num.append(sum)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]

print(n)