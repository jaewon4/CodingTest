import sys
from collections import deque
sys.setrecursionlimit(10**6)
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

# n,m : 정점개수, 간선수
n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
group = [0] * (n+1)

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) 

def dfs(now):
    for next in graph[now]:
        if group[next] == 0:
            group[next] = 1
            dfs(next)
dfs(1)

print(group.count(1) - 1)