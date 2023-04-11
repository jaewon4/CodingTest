import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
from collections import deque
input=sys.stdin.readline

#입력값 받기
N=int(input()) # N이 완제품 번호
V=int(input()) # 어떤 부품을 완성하는데 필요한 부품들 간의 관계수. 즉, 간선 수
graph=[[] for _ in range(N+1)] # 연결정보
indegree=[0]*(N+1) # 부품별 진입차수 0일 경우 기본부품.
# 5행에 [0, 0, 2, 1]이라면 5번 부품을 만드는데 2번부품 2개 3번부품 1개가 필요하다는 의미이다.
needs=[[0]*(N+1) for _ in range(N+1)] # 각 부품이 기본부품 얼마나 필요한지 Matrix

for i in range(V):
    object, part, cnt = map(int,input().split())
    graph[part].append([object, cnt])  # object만드는데 part가 cnt개 필요.
    indegree[object] += 1 # 진입차수 정보모음

q=deque()
basic_parts=[]
for i in range(1, N+1):
    if indegree[i]==0:
        basic_parts.append(i) #기본부품 리스트
        q.append(i)

while q:
    now=q.popleft()
    # object : 만들어야하는 부품 / n : now부품이 몇개가 들어가야 object가 되는지
    for object, n in graph[now]:
        if now in basic_parts:   # 기본부품일경우 목적제품에 +n개
            # 만들어야하는 부품 행에 열이 들어가는 부품번호임
            needs[object][now] += n
        else:
            for i in range(1, N+1):
                # 파트5가 2개 필요하다면 파트5는 2번2개 3번 1개가 필요하다 그러면 곱하기 2를 해주는 부분이다.
                needs[object][i] += needs[now][i] * n
        indegree[object] -= 1
        # 최소 진입차수가 0인 노드를 찾아서 큐에 넣는다.
        if indegree[object]==0:
            q.append(object)

for i in range(N+1):
    if needs[N][i] > 0:
        print(i, needs[N][i])
