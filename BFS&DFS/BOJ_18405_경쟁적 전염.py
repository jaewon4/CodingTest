import sys
from collections import deque
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/시험문제/input.txt", "rt")
input = sys.stdin.readline
# n은 시험관 줄 수, k는 바이러스 수
n, k = map(int, input().split())
v_map = []
for _ in range(n):
    v_map.append(list(map(int, input().split())))

# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력 
s, x, y = map(int, input().split())

tmp = []
# 초기 바이러스 위치를 찾는 부분
for a in range(n):
    for b in range(n):
        if v_map[a][b] != 0 :
            time = 0
            # x좌표, y좌표, 바이러스종류, 시간
            tmp.append((a, b, v_map[a][b], time))
# 오름차순으로 바이러스 이름에 따라 정렬 -> 1번 바이러스부터 퍼지므로
tmp.sort(key = lambda x : x[2])

que = deque(tmp)
dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

while que:
    a, b, virus, cnt_time = que.popleft()
    # 지정한 시간이 되었을때
    if cnt_time == s:
        print(v_map[x-1][y-1])
        exit(0)
    # 4방향(위, 아래, 좌, 우)으로 움직이는 반복문
    for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            # 만약 움직일 위치가 범위를 벗어나면 안되고 움직일 위치에 바이러스가 존재하면 못간다.
            if nx < 0 or nx >= n or ny < 0 or ny >= n or v_map[nx][ny]:
                continue
            else:
                # 움직일 위치에 바이러스를 넣는다.
                v_map[nx][ny] = virus
                # 시간을 증가시키고 움직인 좌표와 바이러스를 큐에 넣어준다.
                que.append((nx, ny, virus, cnt_time+1))

# (X,Y)에 존재하는 바이러스의 종류를 출력 
print(v_map[x-1][y-1])