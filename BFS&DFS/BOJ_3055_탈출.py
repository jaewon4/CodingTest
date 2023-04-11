import sys
from collections import deque
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

# 비버의 굴은 'D'로, 고슴도치의 위치는 'S' 물이 차있는 지역은 '*', 돌은 'X'로 표시 비어있는 곳은 '.'로 표시
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    # 물이 왼쪽에
    for i in range(r):
        for j in range(c):
            # water는 왼쪽에
            if graph[i][j] == "*":
                q.appendleft((i, j))
                visited[i][j] = 0
            # 도치는 오른쪽에 넣는다.
            elif graph[i][j] == "S":
                q.append((i, j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 움직일 위치가 그래프 경계 내에 있는지 확인
            if not 0 <= nx < r or not 0 <= ny < c:
                continue
            # 움직일 위치가 이전에 방문한 적이 있는지 확인
            if visited[nx][ny] != -1:
                continue
            # 움직일 위치가 수원인지 돌인지 확인
            if graph[nx][ny] == "*" or graph[nx][ny] == "X":
                continue
            # 움직일 위치가 비버의 은신처이고 현재의 위치가 수원지인지 확인(수원은 비버은신처에 번지지 않음)
            if graph[nx][ny] == "D" and graph[x][y] == "*":
                continue
            # 움직일 위치가 비버의 은신처이고 현재 위치가 도치의 위치인지 확인
            if graph[nx][ny] == "D" and graph[x][y] == "S":
                # 비버의 집으로가는 경로를 찾은것이며 도치의 위치에서 은신처까지의 최단거리를 반환
                return visited[x][y] + 1
            # 위 조건중 어느것도 충족하지 않으면 움직일 위치를 append한다.
            q.append((nx, ny))
            # 그리고 방문지를 업데이트 하고 graph 에서 * 과 S가 퍼지는것을 표현
            visited[nx][ny] = visited[x][y] + 1
            graph[nx][ny] = graph[x][y]
    return "KAKTUS"

# 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력
# 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력
print(bfs())
