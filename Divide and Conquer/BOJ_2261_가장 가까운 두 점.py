# 이해못했음..........어려음......
import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")
input=sys.stdin.readline
INF = sys.maxsize

# a, b사이 거리의 제곱을 나타내는 함수
def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def recursion(start, end):
    if start == end:
        return INF
    # 종료조건 - 왼, 오에 비교할 점이 하나밖에 없는 경우 ?? 확실치 않음
    elif end - start == 1:
        return distance(point_list[end], point_list[start])
    # 영역을 기준으로 중간 지점 찾기
    middle = (start + end) // 2
    # 왼쪽 pt의 최소 거리 찾기 + 오른쪽 pt 최소 거리 찾기
    d = min(recursion(start, middle), recursion(middle, end))
    # 분할 지점(가운데)으로부터 x좌표가 현재까지의 최소거리 d보다 작은 값이 있나 보기
    # 일단 x축을 기준으로 d 미만인 애들을 target point로 저장
    target_list = []
    for i in range(start, end + 1):
        if (point_list[middle][0] - point_list[i][0]) ** 2 < d:
            target_list.append(point_list[i])
    # target point에서 middle point로부터 일정 거리 미만인 애들 중 가장 작은 값 - min distance
    target_list.sort(key=lambda x:x[1])
    lc = len(target_list)
    for i in range(lc-1):
        for j in range(i + 1, lc):
            dy = (target_list[i][1] - target_list[j][1]) ** 2
            if dy < d:
                d = min(d, distance(target_list[i], target_list[j]))
            else:
                break
    # return 세개 중 최소 거리
    return d

n = int(input())

#점들을 x좌표를 기준으로 오름차순 정렬
point_list = []
for _ in range(n):
    point_list.append(tuple(map(int, input().split())))
point_list.sort()

print(recursion(0, len(point_list)-1))