import sys

input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    input_list = input().split()
    command = input_list[0]
    num = 0
    if len(input_list) == 2:
        num = int(input_list[1])
    
    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
            continue
        else:
            print(stack[-1])
        stack.pop()
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    