n = int(input())
numbers = map(int, input().split())
sosu_count = 0

for num in numbers:
    if num > 1:
        error = 0
        # 에러를 카운트 하는것과 int(제곱근) + 1까지의 범위를 나누어 보는것이 핵심 *************************
        for i in range(2, int(num ** 1/2)+1):
            if num % i == 0:
                error += 1
        if error == 0:
            sosu_count += 1

print(sosu_count)





# 입력받은 배열에서 소수가 아닌것 지우는 방식
# import sys
# sys.stdin.readline()
# nlist = list(map(int, sys.stdin.readline().split()))
# result = nlist[:]
# for n in nlist:
#     if n == 1: 
#         result.remove(n)
#         continue
#     for i in range(2, int(n ** 1/2) + 1):
#         if n%i == 0:
#             result.remove(n)
#             break
# print(len(result))
