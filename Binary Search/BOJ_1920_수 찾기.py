# 이진탐색을 이용한 풀이법
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

def bin_search(a, key):
    first = 0
    end = len(a) - 1

    while True:
        middle = (first + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] < key:
            first = middle + 1
        else:
            end = middle - 1
        if first > end:
            break

    return False

n_list.sort()

for i in range(m):
    if bin_search(n_list, m_list[i]) == True:
        print(1)
    else:
        print(0)

# set을 이용한 풀이법
# n = int(input())
# n_list = set(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# for i in range(m):
#     if m_list[i] in n_list:
#         print(1)
#     else:
#         print(0)