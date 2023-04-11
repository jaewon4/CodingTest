import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    # 이미 dp테이블 정의가 최대로 움직일수 있는 칸이 몇칸인지 적는 곳이므로 탐색을 하는 과정에서
    # 테이블이 이미 채워져 있다면 탐색하지 않아도 된다.
    if dp[x][y]:
        # 이미 한번 왔다간 경로는 그대로 리턴
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위를 벗어나지 않고 움직일 위치의 값이 크다면
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
# 최대로 움직일 수 있는 칸이 몇인지 기록
dp = [[0] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)

# https://www.acmicpc.net/problem/1937
# 욕심쟁이 판다