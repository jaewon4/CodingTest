import sys
input = sys.stdin.readline
num = int(input())

arr = [0] * 10000

for i in range(num):
    a = int(input())
    arr[a - 1] += 1

# ******이부분이 핵심임**************
for i in range(10000):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i + 1)

# 첫쨰줄에 N 수의 개수 1~10,000,000개가
# 둘째줄부터 N개의 수가 주어진다. -> append로 배열에 넣게되면 10,000,000개가 들어간 배열을 만들게 된다.
# 이 수는 10,000보다 작거나 같은 자연수이다. -> 그래서 0이 들어간 10,000가 들어간 배열을 만들어 숫자를 추가해주는 방식은 적은 메모리를 사용한다.
