import sys
from collections import deque
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

n, k = map(int, input().split())
que = deque()
result = list()

for i in range(1, n + 1):
    que.append(i)

while que:
    for i in range(k - 1):
        que.append(que.popleft())
    result.append(que.popleft())

print("<",end='')
for i in range(len(result)-1):
    print(f"{result[i]}, ", end='')
print(result[-1], end='')
print(">")

