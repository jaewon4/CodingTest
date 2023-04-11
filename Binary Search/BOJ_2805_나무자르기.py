# n : 나무수 , m : 필요나무길이
n, m = map(int, input().split())
trees = list(map(int, input().split()))
# 자를 나무의 길이 선정을 위한 변수
# 즉, 자를 나무 길이를 이진탐색 한다.
start , end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    # 잘린 나무의 길이
    cut_length = 0
    # 잘라보고 자른 길이를 더하는 반복문
    for tree in trees:
        if tree > mid:
            cut_length += tree - mid
    
    if cut_length == m:
        end = mid
        break
    # 너무 많이 잘리면 start값을 더 높여서 더 조금 자르게 해야함 
    elif cut_length > m:
        start = mid + 1
    # 필요 길이보다 더 조금 잘리면 나무를 자를 길이를 줄여야 하므로
    # 줄여야 더 많이 잘라갈수있음
    else:
        end = mid - 1

# M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
print(end)