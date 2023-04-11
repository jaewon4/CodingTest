import heapq
import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수(도시의개수)
n = int(input())
# 간선의 개수(버스의 개수)
m = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

st, ed = map(int, input().split())

# 최단 거리 테이블을 모두 무한으로 초기화
# 이 배열은 예를 들면 distance[2]의 값이 의미하는 것은 2번 노드까지 가는데 걸리는 최소비용을 나타낸다.
distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # 이 큐에는 (비용, 현재노드) 가 들어간다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        # (비용, 현재노드)
        n_cost, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 노드가 이미 더 짧은 거리로 방문한 적이 있는지 확인
        # 예를들면 1번노드에서 출발하여 2번을 거쳐 3을 갔는데 비용이 2라면 distance[now] = 2이다
        # 그런데 1번노드에서 출발하여 4번을 거쳐 3을 갔는데 비용이 4라면 n_cost=4로 continue로 넘어가준다.
        if distance[now] < n_cost:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 전부 비용을 계산해서 큐에 넣는다. + distance배열을 갱신함
        # 즉, heapq에 넣음으로서 (cost, dest)순서로 넣음으로 최소힙이 만들어지고 
        # 항상 큐에는 최소 cost를 가진 데이터가 먼저 pop되게 된다.
        # dest, wei => 종착지, 비용
        for dest, wei in graph[now]:
            cost = distance[now] + wei
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[dest] > cost:
                distance[dest] = cost
                # 갱신된 비용과 목적지를 넣어준다.
                heapq.heappush(q, (cost, dest))

# 다익스트라 알고리즘을 수행
dijkstra(st)
# 출발 도시에서 도착 도시까지 가는데 드는 최소 비용
# 즉 ed까지의 최소비용을 출력
print(distance[ed])
