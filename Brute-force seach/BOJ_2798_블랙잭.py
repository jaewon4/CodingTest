import sys

input = sys.stdin.readline
n, m = map(int, input().split())
card_list = list(map(int, input().split()))
sum_list = list()

for i in range(len(card_list)):
    for j in range(len(card_list)):
        for k in range(len(card_list)):
            if i == j or j == k or k == i:
                pass
            elif card_list[i] + card_list[j] + card_list[k] <= m:
                sum_list.append(card_list[i] + card_list[j] + card_list[k])

max = max(sum_list)
print(max)

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# cards.sort()
# ans = 0
# for i in range(N-1, 1, -1):
#     for j in range(i-1, 0, -1):
#         for k in range(j-1, -1, -1):
#             total = cards[i] + cards[j] + cards[k]
#             if total <= M:
#                 ans = max(ans, total)
#                 break
# print(ans)

# from itertools import permutations
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# _list = list(map(int, input().split()))

# result = 0

# per = permutations(_list, 3)

# for i in per:
#     if sum(i) > result and sum(i) <= m:
#         result = sum(i)

# print(result)


