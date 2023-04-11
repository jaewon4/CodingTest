import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input=sys.stdin.readline

# 테스트 케이스 수
t = int(input())

for _ in range(t):
    # 동전의 가지수
    n = int(input())
    # 동전 금액
    coins = list(map(int, input().split()))
    # 목표 금액
    m = int(input())
    # 목표 금액만큼 dp생성 -> dp[m]으로 방법의 수를 출력 할 것임
    dp = [0] * (m + 1)
    # 모든 경우의 동전이어도 0개의 동전을 이용하면 0원은 무조건 만들수 있으므로
    dp[0] = 1
    # N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한 줄에 하나씩 출력
    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]
    
    print(dp[m])

# 정리 잘되있음!
# https://d-cron.tistory.com/23



