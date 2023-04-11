import sys
input = sys.stdin.readline

# 배열의 길이
n = int(input())
paper = []
# arr에 1, 0이 들어간 배열 삽입
for _ in range(n):
    paper.append(list(map(int, input().split())))
result = []

# x, y왼쪽 끝부분의 좌표를 넣는 변수
# n은 종이 길이
def cut(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                # 1사분면
                cut(x, y, n // 2)
                # 2사분면
                cut(x, y + n // 2, n // 2)
                # 3사분면
                cut(x + n // 2, y, n // 2)
                # 4사분면
                cut(x + n // 2, y + n // 2, n // 2)
                return
    result.append(color)
    return

cut(0, 0, n)
print(result.count(0))
print(result.count(1))
