import sys
from collections import deque
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

# 수빈, 동생
n, k = map(int, input().split())
que = deque()
que.append(n)
visited = [0] * 100001

while que:
    now = que.popleft()
    move = [now + 1, now -1, now * 2]
    if now == k:
        print(visited[k])
        exit()
    for i in move:
        if 0 <= i < 100001 and not visited[i]:
            # visited[now]는 현재 시간을 얼마나 썼는지 추적할수 있게 해준다.
            # visited는 매초 어느 거리에 갔었는지 추적하는 배열임
            visited[i] = visited[now] + 1
            que.append(i)
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력