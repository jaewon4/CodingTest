import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9

# DFS 풀이는 연산자의 갯수만큼 탐색을 하며, 연산자가 존재하면 그 연산을 수행하며 재귀호출을 통해 탐색을 진행
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum
    global minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    # 첫 연산기호를 4가지 전부 적용해보는 구간
    # 전부 if문인 이유는 만약 1 2 3 인풋이라면 1 2사이 4가지 부호가 모두 들어갈수
    # 있기때문에 if로 해줘야 모든 경우를 dfs로 탐색가능하다.
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
