from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = 0
per = permutations(a)

for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    if s > ans:
        ans = s

print(ans)

# from itertools import permutations
# import sys

# def calcu(arr):
#     sum = 0
#     for i in range(len(arr)-1):
#         sum += abs(arr[i]-arr[i+1])
#     return sum

# input = sys.stdin.readline

# n = int(input())

# _list = list(map(int, input().split()))

# result = 0

# per = permutations(_list)

# for i in per:
#     if result < calcu(i):
#         result = calcu(i)

# print(result)


