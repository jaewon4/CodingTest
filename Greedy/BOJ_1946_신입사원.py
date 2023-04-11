import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    student = [list(map(int,input().split()))for _ in range(n)]
    student.sort()
    end = student[0][1]
    cnt = 1
    for i in range(1, n):
        if student[i][1] < end:
            cnt += 1
            end = student[i][1]
    print(cnt)
