import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 구슬 개수 N, 저울에 올려본 쌍수 M
N, M = map(int, sys.stdin.readline().split())
# 나보다 무거운 구슬, 가벼운 구슬 리스트를 만듬
# -> 만약 나보다 무거운/가벼운 구슬이 (N+1)/2개 있다면 해당 구슬은 중간구슬이 될 수 없음!
heavy_list = [[] for _ in range(N + 1)]
light_list = [[] for _ in range(N + 1)]

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_list[light].append(heavy)
    light_list[heavy].append(light)

def dfs(now, list):
    global check
    visited[now] = True
    for i in list[now]:
        if not visited[i]:
            check += 1
            dfs(i, list)
# 중간값이 될수 없는 애들의 개수를 위한 변수
count = 0
# md보다 많은 수의 무겁거나 가벼운 애들이 있다면 절대 중간값이 될수 없는 값이다.
mid = (N + 1) / 2
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    # check값이 무거운애들만큼 +해준거
    check = 0
    dfs(i, heavy_list)
    if (check >= mid):
        count += 1
    # visited 초기화 안해도 정답인 이유가 뭐야??????
    visited = [False] * (N + 1)
    # check는 가벼운애들 개수가 나온다.
    check = 0
    dfs(i, light_list)
    if check >= mid:
        count += 1
print(count)