# 소수 판별 함수
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    case_num = int(input())
    a, b = case_num // 2, case_num // 2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(f'{a} {b}')
            break
        else:
            a -= 1
            b += 1



# # 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
# n = int(input())
# sosu_1 = 0
# sosu_2 = 0

# # 특정 수 N이 소수인지 아닌지 구하는 법은 2부터 N-1 까지의 수로 해당 수를 나눠보고, 이 과정에서 어떠한 수에 의해 나누어 떨어지는지 확인하는 것
# def is_prime_num(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

# for _ in range(n):
#     # num은 짝수
#     num = int(input())
#     sosu_list = list()

#     # num의 소수리스트 저장
#     for i in range(2, num):
#         if is_prime_num(i) == True:
#             sosu_list.append(i)

#     print(sosu_list)

#     for sosu in sosu_list:
#         results = list()

#         if sosu * 2 == num:
#             print(sosu, sosu)
#             break
#         elif num % sosu != 1 and num // sosu == 1:
#             sosu_1 = num % sosu
#             sosu_2 = sosu
#             print(sosu_1, sosu_2)
#             results.append([sosu_1, sosu_2])
