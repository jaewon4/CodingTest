# 이분 그래프가 뭔지 알아야 하는 문제!!!
import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
k = int(input())

def dfs(now, group):
    # 방문한 노드에 group할당
    visited[now] = group
    for next in graph[now]:
        # 아직 안가본 곳이면 방문
        if visited[next] == 0:
            # 이부분이 이해가 잘안가네....
            # dfs가 false이면 return false인데
            # 그냥 return dfs(next, -group)해도되는거아닌가?
            if not dfs(next, -group):
                return False
        # 이전에 방문한 곳인데 그룹이 동일하면 False
        elif visited[next] == visited[now]:
            return False
    return True

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    flag = True

    # 1~v노드 까지 dfs로 방문
    for i in range(1, v + 1):
        if visited[i] == 0:
            flag = dfs(i, 1)
            # 하나라도 flag가 false가 나오면 루프를 탈출하는 조건문!
            if not flag:
                break

    print('YES' if flag else 'NO')
