import sys
from collections import deque
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

input = sys.stdin.readline
n = int(input())
que = deque()

for _ in range(n):
    input_list = list(input().split())
    command = input_list[0]
    number = 0
    if len(input_list) > 1:
        number = input_list[-1]
    
    if command == 'push':
        que.append(number)
    elif command == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            que.popleft()
    elif command == 'size':
        print(len(que))
    elif command == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif command == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

