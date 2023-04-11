N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")



# number, min_number = map(int, input().split())
# number_arry = list(map(int, input().split()))

# result = list()

# for i in range(number):
#     if number_arry[i] < min_number:
#         result.append(str(number_arry[i]))

# a = " ".join(result)
# print(a)
