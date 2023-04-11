import sys
from collections import deque
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수 쌓아올려지는 상자의 수를 나타내는 H
m, n, h = map(int, input().split())
# 1 토마토, 0 익지 않은 토마토, -1 들어있지 않은 칸
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
que = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                # 익은 토마토 좌표를 큐에 저장
                que.append([i, j, k])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while que:
    x, y, z = que.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if graph[nz][nx][ny] == 0:
                # 더하기 1해주는것이 몇일이 지났는지를 추적할수있는 포인트
                graph[nz][nx][ny] = graph[z][x][y] + 1
                que.append([nx, ny, nz])
ans = 0
for arr in graph:
    for line in arr:
        for tomato in line:
            if tomato == 0:
                # 안익은 토마토가 있으면 바로 정지
                print(-1)
                exit()
        ans = max(ans, max(line))

# 1에서 시작했기 떄문에 값에서 1뺴주기
print(ans - 1)




