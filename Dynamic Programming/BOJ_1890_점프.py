import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [ [0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if map[i][j] != 0:
            jump = map[i][j]
            if i+jump < N:
                dp[i + jump][j] += dp[i][j]
            if j+jump < N:
                dp[i][j+jump] += dp[i][j]
print(dp[N-1][N-1])

# 점프
# https://www.acmicpc.net/problem/1890