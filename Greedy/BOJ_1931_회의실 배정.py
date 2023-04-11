import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    st, ed = map(int, input().split())
    time.append([st, ed])

# 2, 2 -> 1, 2가 나오면 cnt가 1이 올라가지만 반대의 경우 2가 되므로 람다로 정렬
time.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)

# https://www.youtube.com/watch?v=vw4gqeM4UGs
# https://www.youtube.com/watch?v=7noZLdfHIMQ