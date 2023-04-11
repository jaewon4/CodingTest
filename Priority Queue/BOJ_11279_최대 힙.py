import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        try:
            # -값이 들어있으므로
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)




# #  시간초과
# import sys

# input = sys.stdin.readline
# n = int(input())
# num_list = list()

# for _ in range(n):
#     num = int(input())
    
#     if num == 0 and num_list:
#         max_num = max(num_list)
#         index = num_list.index(max_num)
#         num_list.pop(index)
#         print(max_num)
#         continue
#     elif num == 0:
#         print(0)
#         continue

#     num_list.append(num)