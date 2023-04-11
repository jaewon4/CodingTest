import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

# 물품수 n 버틸수 있는 무게 k
n, k = map(int, input().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# 각 물건의 무게 w 해당 물건의 가치 v
w = [0]
v = [0]
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(1, n+1):
    for j in range(1, k+1):
        if w[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값
print(dp[-1][-1])