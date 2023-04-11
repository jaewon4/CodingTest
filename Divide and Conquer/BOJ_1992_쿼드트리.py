import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
result = []

def cut(x, y, N):
    color = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != arr[i][j]:
                result.append('(')
                cut(x, y, N // 2)
                cut(x, y + N // 2, N // 2)
                cut(x + N // 2, y, N // 2)
                cut(x + N // 2, y + N // 2, N // 2)
                result.append(')')
                return
    if color == '1':
        result.append('1')
    else:
        result.append('0')

cut(0, 0, n)

for i in result:
    print(i, end="")
print()