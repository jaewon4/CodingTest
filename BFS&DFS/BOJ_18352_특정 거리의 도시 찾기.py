import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    # 같은 최단거리를 가질수 있어서 배열로 선언
    answer = []
    # 큐에 하나의 노드씩 넣어서 탐색
    q = deque([start])
    # 첫번쨰를 방문처리 -> 방문하면 다시가면 안됨
    visited[start] = True
    # 얼만큼 움직였는지 기록용 distance
    distance[start] = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                distance[next] = distance[now] + 1
                # 즉, 도달할수있는 도시의 번호를 출력
                if distance[next] == k:
                    answer.append(next)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)