import sys
from collections import deque
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
# 진입차수 : 특정노드가 있을때 그 노드로 들어오는 다른 노드의 개수
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 진입차수를 1증가
    in_degree[b] += 1
    # 정점 a에서 b로 이동 가능
    graph[a].append(b)

que = deque()
ans = []

# 최초 진입차수가 0인 노드 탐색해서 큐에 넣는다.
for i in range(1, n + 1):
    if in_degree[i] == 0:
        que.append(i)

while que:
    # 현재 방문노드 저장
    current = que.popleft()
    ans.append(current)
    # 방문한 노드의 간선을 제거하는 부분
    for x in graph[current]:
        in_degree[x] -= 1
        # 진입차수가 0이면 큐에 넣는다.
        if in_degree[x] == 0:
            que.append(x)

print(*ans, end=" ")
