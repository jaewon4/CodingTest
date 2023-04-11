import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

n = int(input())
dp = [0] * 1001
num_list = list(map(int, input().split()))

for num in num_list:
    dp[num] = max(dp[:num]) + 1

print(max(dp))