import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

n, k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)

for coin in reversed(coins):
    cnt += k // coin
    k %= coin

print(cnt)