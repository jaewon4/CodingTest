import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

# n개의 줄에 m개의 정수가 주어진다.
n, m = map(int, input().split())
# 1은 이동가능 0은 벽
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def bfs(x, y):
    # 왼, 오, 아래, 위
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        # 현재 위치에서 4가지 방향 위치확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 위치가 벗어나면 안되기떄문
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이므로 진행불가
            if graph[nx][ny] == 0:
                continue
            # 벽이 아니므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
        
    return graph[n-1][m-1]

print(bfs(0, 0))