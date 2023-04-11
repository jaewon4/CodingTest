import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

import heapq

n = int(sys.stdin.readline())
cards = []
result = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(cards, num)
# 저장한 값을 다시 cards에 넣어둬야함 그래야 합친 카드뭉치를 다시 다른 뭉치랑 합치는데 소모되니까
if len(cards) == 0 or len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)
    print(result)
    