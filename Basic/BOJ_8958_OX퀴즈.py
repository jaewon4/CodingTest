n = int(input())

for _ in range(n):
    ox_list = input()
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

# # 받은 숫자만큼 입력을 받아 리스트에 저장
# while n > 0:
#     n -= 1
#     a = list(input())
#     case.append(a)

# # 리스트에 있는 문제를 점수로 만들기
# index = len(case)
# counter = 0
# score = 0
# my_score = 0

# for i in range(len(case)):
#     for j in range(len(case[i])):
#         if case[i][j] == "O":
#             score += 1
#             my_score += score
#         else:
#             score = 0       
#     print(my_score)

#     score = 0  
#     my_score = 0