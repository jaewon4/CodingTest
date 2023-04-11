import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")
input = sys.stdin.readline

# 사대의 수, 동물의 수, 사정거리,
m, n, l = map(int, input().split())
# 사로의 사람위치
gun = list(map(int, sys.stdin.readline().split()))
# 동물위치
animal = list(map(int, sys.stdin.readline().split()) for _ in range(n))
gun.sort()
cnt = 0

for x, y in animal:
    # y좌표가 l보다 크면 범위를 벗어나므로 제외
    if (y>l):
        continue

    # 각 동물위치 기준 가능한 사로 start, end지점 산출
    s = x+y-l
    e = x-y+l
    
    # 사로의 사람 위치를 이진탐색을 해서 어떤사로가 사냥감이 잡히는 사로인지 탐색
    # 하기 위해서 gun리스트를 탐색할 인덱스를 나타낸다.
    left, right = 0, m-1

    while left <= right:
        mid = (left+right)//2
        if gun[mid] >= s and gun[mid] <= e:
            cnt += 1
            break
        elif gun[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
print(cnt)
