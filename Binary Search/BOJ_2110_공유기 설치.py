n,c = map(int,input().split())

house = []
for _ in range(n):
    x = int(input())
    house.append(x)

house.sort()

# 좌표값의 최소값
start = 1
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]
# 가장 인접한 두 공유기 사이의 최대 거리
result = 0

while start <= end:
    # 공유기 사이의 거리
    mid = (start + end) // 2
    # 공유기 설치한곳 기록용
    current = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= current + mid:
            current = house[i]
            count += 1
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)