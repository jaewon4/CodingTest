import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def melt(x, y):
    cnt = 0  # 인접한 바다 개수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                cnt += 1
    if cnt != 0:
        return x, y, cnt
    else:
        return None

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] != 0:
                dfs(nx, ny)

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# 풀이
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
while True:
    answer += 1
    # 1. 빙하 녹이기
    reduce = []  # x, y, 녹는 높이
    for x in range(1, N):
        for y in range(1, M):
            if graph[x][y] != 0:
                h = melt(x, y)
                if h is not None:
                    reduce.append(h)
    for x, y, h in reduce:
        graph[x][y] = graph[x][y] - h if graph[x][y] - h > 0 else 0
    # 2. 빙하 개수 구하기
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for x in range(1, N):
        for y in range(1, M):
            if graph[x][y] != 0 and not visited[x][y]:
                cnt += 1
                if cnt == 2:
                    break
                dfs(x, y)
    if cnt > 1:  # 종료 조건
        break
    # 첫줄과 마지막줄은 어차피 0으로 된 경계이므로 제외하고 나머지 부분을 
    # 다 더해서 0이라면 빙하가 다 녹은것으로 판단하기 위한 조건문임
    # 문제에서 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력하기때문
    if sum(map(sum, graph[1:-1])) == 0:
        answer = 0
        break
# 빙산이 분리되는 최초의 시간(년)을 출력
print(answer)