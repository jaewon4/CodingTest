import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
A = input().rstrip()
graph = [[] for _ in range(n+1)]
# 각노드가 실외인지 실내인지 확인하는 배열 
# 0: 실외 1: 실내
place = [0] * (n+1)
visited = [0] * (n+1)

for i in range(len(A)):
    if A[i] == '1':
        place[i+1] = 1

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node):
    res = 0 
    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                res += dfs(next_node)
        else:
            res += 1
    return res

ans = 0

# 모든 노드를 순회하기 위한 for문
# else부분을 위한거라 보면됨
for i in range(1, n+1):
    # 실외를 찾는 조건문
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            # 실외노드에 붙어있는 실내노드의 개수를 통해서 경우의 수를 구할수 있음
            # res * (res - 1)이다.
            ans += res * (res - 1)
    else:
        # 실내노드끼리 붙어있는 경우를 처리하기 위한 부분
        for next_node in graph[i]:
            if place[next_node] == 1:
                ans += 1
print(ans)