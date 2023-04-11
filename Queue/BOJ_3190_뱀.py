import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")
from collections import deque
input = sys.stdin.readline

# snake - 덱으로 가장 앞에는 머리, 가장 끝은 꼬리
snake = deque([[1, 1]])
mark = deque([])
# direction - 이차원 배열, 초와 방향을 지정
direction = deque([])

N = int(input())
apple = int(input())
for _ in range(apple):
    i = list(map(int, input().split()))
    mark.append(i)
    
L = int(input())
for _ in range(L):
    direction_list = list(input().split())
    direction.append(direction_list)

# 종료 조건 - snake 머리(덱 가장 앞)가 벽이나 몸에 닿을 경우
# 초
cnt = 0
# 북 동 남 서
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 초기방향 1
d_index = 1
while 0 < snake[0][0] <= N and 0 < snake[0][1] <= N:
    next_head = [0, 0]
    if direction and int(direction[0][0]) == cnt:
        if direction[0][1] == 'D':
            d_index += 1
        else:
            d_index -= 1
        direction.popleft()
    d_index = d_index % 4
    next_head[0] = snake[0][0] + d[d_index][0]
    next_head[1] = snake[0][1] + d[d_index][1]
    cnt += 1
    if next_head in snake:
        break
    # 사과 처리
    if next_head not in mark:
        snake.pop()
    else:
        mark.remove(next_head)
    snake.appendleft(next_head)
print(cnt)

# import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")
# from collections import deque

# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append([0] * n)

# k = int(input())
# apple = []
# for _ in range(k):
#     a, b = map(int, input().split())
#     apple.append([a - 1, b - 1])
#     lst[a - 1][b - 1] = 1

# l = int(input())
# move = []
# for _ in range(l):
#     x, c = input().split()
#     move.append([int(x), c])

# snake = deque()
# snake.append([0, 0])
# direction = 0
# time = 0

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# while True:
#     time += 1
#     x, y = snake[-1]
#     nx, ny = x + dx[direction], y + dy[direction]

#     if nx < 0 or nx >= n or ny < 0 or ny >= n:
#         break  # snake hits the wall

#     if [nx, ny] in snake:
#         break  # snake hits its body

#     snake.append([nx, ny])

#     if lst[nx][ny] == 1:
#         lst[nx][ny] = 0
#     else:
#         snake.popleft()

#     if move and time == move[0][0]:
#         _, c = move.pop(0)
#         if c == 'D':
#             direction = (direction + 1) % 4
#         else:
#             direction = (direction - 1) % 4

# print(time)