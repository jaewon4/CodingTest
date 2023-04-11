import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# n : 노드의 수
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def dfs(root):
    for next in graph[root]:
        if visited[next] == 0:
            visited[next] = root
            dfs(next)

dfs(1)
for i in range(2, n + 1):
    print(visited[i])