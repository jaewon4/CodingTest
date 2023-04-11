# 모범답안
origin = input()
target = int(origin)
cycle = 0
new = -1
while True:
    cycle += 1
    if len(origin) == 1:
        origin = '0'+origin
    new = origin[-1] + str(int(origin[0])+int(origin[1]))[-1]
    if target == int(new):
        break
    origin = new

print(cycle)


# 시험제출했던 문제
# 너무 많은 코드로 풀었음.......
# import sys
# input = sys.stdin.readline
# n = int(input())
# cnt = 0
# n_str = str(n)

# while True:
#     cnt += 1
#     if len(n_str) == 1:
#         ones = 0
#         seconds = int(n_str[0])
#     else :
#         ones = int(n_str[0])
#         seconds = int(n_str[1])

#     sum_ab = ones + seconds
#     # 분리
#     sum_ab = str(sum_ab)
#     if len(sum_ab) > 1:
#         sum_ones = sum_ab[0]
#         sum_seconds = sum_ab[1]
#     else:
#         sum_seconds = sum_ab[0]

#     result = []

#     result.append(str(seconds))
#     result.append(sum_seconds)

#     sum_ab = int(''.join(result))

#     n_str = str(sum_ab)

#     if sum_ab == n:
#         break

# print(cnt)