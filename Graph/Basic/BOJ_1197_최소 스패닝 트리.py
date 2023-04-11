# 이 문제는 형태를 외워두기!!!!!!!!!!!!!!!!!!!!!!
import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
# Kruskal Algorithm
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
# C(Cost)가 적은 것부터 정렬
edges.sort(key=lambda x: x[2])
# 유니온 파인드를 하기 위해서 각 노드가 자기자신을 가리키는 배열을 선언
# 이 배열로 parent를 추적해나간다.
parent = [i for i in range(V+1)]
# Union-Find : 합치고 찾고
# 부모가 뭔지 보는 함수(find)
def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]
# 부모가 같지않으면 연결하는 함수(union)
def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b        

answer = 0
for a, b, cost in edges:
    # cost가 작은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을 때(사이클 없을 때)만 확정
    if find_parent(a, parent) != find_parent(b, parent):
        union_parent(a, b, parent)
        answer += cost
print(answer)