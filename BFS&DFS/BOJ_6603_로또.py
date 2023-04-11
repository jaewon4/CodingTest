from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    n_list = list(map(int, input().split()))
    
    if n_list[0] == 0:
        break

    num_length = n_list[0]
    n_list = n_list[1:]

    com = combinations(n_list, 6)

    for i in com:
        print(*i)

    print()

# DFS 사용 풀이법
# import sys

# input = sys.stdin.readline
# lotto = []

# def dfs(lotto, visited):
#     if len(lotto) == 6:
#         for i in range(6):
#             print(nums[lotto[i]], end=' ')
#         print()
#         return

#     t_visited = visited[:]
#     for i in range(len(t_visited)):
#         if not t_visited[i]:
#             t_visited[i] = True
#             dfs(lotto + [i], t_visited)

# while True:
#     nums = list(map(int, input().split()))
#     if len(nums) == 1 and nums[0] == 0:
#         break

#     length = nums.pop(0)

#     visited = [False] * len(nums)
#     dfs(lotto, visited)
#     print()