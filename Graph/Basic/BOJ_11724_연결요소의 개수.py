import sys
from collections import deque
sys.setrecursionlimit(10**6)
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

# n,m : 정점개수, 간선수
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
# 그룹의 해당 숫자는 그룹 번호를 의미합니다.
# [0, 1, 1, 1, 2, 2, 2, 3] => 3개의 그룹으로 구성되어있음
# 즉, 연결요소의 숫자는 3이라는 의미입니다.
group = [0] * (n+1)

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) 

def dfs(now, group_num):
    for next in graph[now]:
        if group[next] == 0:
            group[next] = group_num
            dfs(next, group_num)

cnt = 1
for i in range(1, n+1):
    if group[i] == 0:
        group[i] = cnt
        # 처음은 1번레이블인 노드를 찾는 dfs
        dfs(i, cnt)
        # 끝이나면 2번레이블을 갖는 노드를 찾는다.
        cnt += 1

print(max(group))