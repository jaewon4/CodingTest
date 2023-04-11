import sys

input = sys.stdin.readline
nanjang_list = []
one = 0
two = 0

for _ in range(9):
    nanjang_list.append(int(input()))

sum_val = sum(nanjang_list)

for i in range(9):
    for j in range(9):
        if sum_val - (nanjang_list[i] + nanjang_list[j]) == 100:
            one = nanjang_list[i]
            two = nanjang_list[j]

nanjang_list.remove(one)
nanjang_list.remove(two)
nanjang_list.sort()

for nanjang in nanjang_list:
    print(nanjang)


# from itertools import permutations
# import sys

# input = sys.stdin.readline
# _list = []

# for _ in range(9):
#     _list.append(int(input()))

# per = permutations(_list, 7)

# success = []

# for i in per:
#     if sum(i) == 100:
#         success = list(i)

# success.sort()

# for i in success:
#     print(i)
