import sys
from collections import deque
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

n = int(input())
que = deque()

for i in range(1, n + 1):
    que.append(i)

while len(que) > 1:
    que.popleft()
    num = que[0]
    que.append(num)
    que.popleft()

print(que[0])
