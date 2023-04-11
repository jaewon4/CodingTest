import sys

# a를 b번 제곱하여 c로 나눈 나머지를 출력!
a, b, c = map(int, input().split())

def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n//2)
        if n % 2 == 1:
            return (tmp * tmp * a) % c
        else:
            return (tmp * tmp) % c

print(multi(a, b))




# 시간초과
# import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

# a, b, c = map(int, input().split())

# for _ in range(a):
#     a *= a

# result = a % c
# print(result)
