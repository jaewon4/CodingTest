import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

import heapq

n = int(sys.stdin.readline())
# 최대힙 -> pop하면 중간값이 나온다.
left_heap = []
# 최소힙
right_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    if right_heap and right_heap[0] < -left_heap[0]:
        left_val = heapq.heappop(left_heap)
        right_val = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right_val)
        heapq.heappush(right_heap, -left_val)
    
    print(-left_heap[0])
