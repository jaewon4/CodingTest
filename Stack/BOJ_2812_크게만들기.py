import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

n, k = map(int, input().split())
str_num = list(input())
stack = []

for i in range(n):
    while stack:
        if stack[-1] < int(str_num[i]) and k > 0:
            stack.pop()
            k -= 1
        else:
            break
    
    stack.append(int(str_num[i]))

while k > 0:
    stack.pop()
    k -= 1

result = ''.join(str(_) for _ in stack)
print(int(result))
