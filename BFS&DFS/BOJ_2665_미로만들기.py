import sys
import heapq
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 우선순위 큐를 사용했을 때 원소를 pop하면, 작은 값이 먼저 반환되므로 
    # 검은 방이 아닌 곳을 방문하려고 하고, 만약 모두 방문했을 때 검은 방이 아닌 곳을 방문하게 된다.
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    # 첫번째는 무조건 흰방(1)임
    visited[0][0] = 1
    while heap:
        # a : 방 색상 변경의 최소 수 / x, y : 그리드를 탐색하는 동안 현재 방의 위치를 ​​추적
        a, x, y = heapq.heappop(heap)
        # 오른쪽 대각선 끝부분에 도달하면 a를 출력하고 리턴
        if x == n - 1 and y == n - 1:
            # 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.
            print(a)
            return
        # 4방향으로 시작지점에서부터 움직이는 반복문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny의 범위를 지정하고 그 범위 안에 있으면서 방문처리가 되지 않은 곳이라면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if room[nx][ny] == 0:
                    # 움직일 곳이 0이라면 즉, 검은방 이라면 비용에 +1을 하여 힙에 저장
                    heapq.heappush(heap, [a + 1, nx, ny])
                else:
                    # 움직일곳이 1이라면 즉, 흰방 이라면
                    heapq.heappush(heap, [a, nx, ny])

dijkstra()
