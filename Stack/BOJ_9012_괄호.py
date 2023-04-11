import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

input = sys.stdin.readline

n = int(input())


for _ in range(n):
    input_list = list(input().rstrip())
    stack = []
    for i in input_list:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

