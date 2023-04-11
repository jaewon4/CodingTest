import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

one = '0' + input().rstrip()
two = '0' + input().rstrip()
n = len(one)
m = len(two)
dp = [[0] * (m) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if one[i] == two[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[n-1][m-1])


# import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
# input=sys.stdin.readline

# string_one = input().rstrip()
# string_two = input().rstrip()
# n = len(string_one)
# m = len(string_two)

# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if string_one[i-1] == string_two[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# print(dp[n][m])

# 강의 점화식 설명 잘되어있음
# https://www.youtube.com/watch?v=EAXDUxVYquY