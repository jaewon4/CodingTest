import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

input = sys.stdin.readline

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, B//2)
    # 지수가 홀수이면
    if B % 2 == 1:
        return mul(mul(tmp, tmp), A)
    # 지수가 짝수이면
    else:
        return mul(tmp, tmp)

result = square(A, B)
for r in result:
    print(*r)