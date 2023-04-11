import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    x, y = map(int, input().split())
    print(x + y)
