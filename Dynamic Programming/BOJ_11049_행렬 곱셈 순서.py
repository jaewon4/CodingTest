import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]

for j in range(1, n):
    for i in range(n - j):
        # 첫번째 대각선을 채운다.
        if j == 1:
            dp[i][i + j] = matrix[i][0] * matrix[i][1] * matrix[i+j][1]
            continue

        # min값을 dp에 넣기위해 큰 수를 넣고 시작
        # 0이 있으면 0이 min값이라 min값이 제대로 들어가지 않는다.
        dp[i][i+j] = 2**32

        # 나머지 대각선을 채운다.
        for k in range(i, i+j):
            dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+j] + matrix[i][0] * matrix[k][1] * matrix[i+j][1])

print(dp[0][n-1])

# https://www.youtube.com/watch?v=8Ni1gaP35i8