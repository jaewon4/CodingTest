import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

n = int(input())
d = [0] * 91

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    # fibo(x - 1)는 재귀로 종료조건까지 내려가고 뒤에 fibo(x - 2)는 
    # 위의 if d[x] != 0를 통해서 dp에서 값을 가져온다.
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(n))


# 인프런 강의
# 딕셔너리를 이용한 방법(탑다운방식)
# import sys
# input=sys.stdin.readline

# n = int(input())

# memo = {}
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if n not in memo:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]

# print(fibo(n))


# 딕셔너리를 이용한 방법(바텀업방식)
# import sys
# input=sys.stdin.readline

# n = int(input())
# memo = {1: 1, 2: 2}
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     for i in range(3, n+1):
#         memo[i] = memo[i-1] + memo[i-2]
#     return memo[n]

# print(fibo(n))







# # 탑다운 방식 : 재귀합수 사용

# d = [0] * (100)

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

# print(fibo(99))


# # 바텀업 방식 : 반복문 사용

# d = [0] * 100
# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3, n + 1):
#     d[i] = d[i - 1] + d[i - 2]

# print(d[n])