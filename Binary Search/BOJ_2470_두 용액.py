# # 이진탐색을 이용한 풀이
# import sys

# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()  # 배열 정렬

# left = 0
# right = n - 1
# result = [sys.maxsize, sys.maxsize]  # 두 용액의 합의 최솟값을 저장할 리스트

# while left < right:
#     sum_value = arr[left] + arr[right]
#     if abs(sum_value) < sum(result):  # 현재 합이 최솟값보다 작으면 결과 리스트 갱신
#         result = [arr[left], arr[right]]
#     if sum_value < 0:  # 합이 0보다 작으면 왼쪽 용액을 더 큰 수로 변경
#         left += 1
#     else:  # 합이 0보다 크면 오른쪽 용액을 더 작은 수로 변경
#         right -= 1

# print(result[0], result[1])



# 2pointer를 이용한 풀이
import sys
read = sys.stdin.readline

n = int(read())
solution_list = sorted(list(map(int, read().split())))
        
#start, end가 처음에는 양쪽 끝 원소들을 가리킴
start = 0
end = len(solution_list) - 1
close_zero = 1e10
left_num = 0
right_num = 0

while start < end:
    #만약 두 원소의 합이 음수이면 start + 1
    if solution_list[start] + solution_list[end] < 0:
        if abs(solution_list[start] + solution_list[end]) < close_zero :
            close_zero = abs(solution_list[start] + solution_list[end])
            left_num = solution_list[start]
            right_num = solution_list[end]
        start += 1
    #두 원소의 합이 양수이면 end - 1
    elif solution_list[start] + solution_list[end] > 0:
        if solution_list[start] + solution_list[end] < close_zero:
            close_zero = solution_list[start] + solution_list[end]
            left_num = solution_list[start]
            right_num = solution_list[end]
        end -= 1
    # 이부분이 있어야 시간초과가 안난다.
    if solution_list[start] + solution_list[end] == 0:
        left_num = solution_list[start]
        right_num = solution_list[end]
        break

print(left_num, right_num)