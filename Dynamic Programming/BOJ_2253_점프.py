import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input = sys.stdin.readline

# N : 돌 개수, M : 작은돌 개수
N, M = map(int, input().split())
# dp : 첫 번째 돌에서 N 번째 돌에 도달하는 데 필요한 최소 이동 수를 저장하는 데 사용
# int((2 * N)** 0.5) + 1 :  N에 도달했을 때의 속도의 근사값
# 왜 + 2인거지??? => 아래 dp에서 j + 1까지 검사하기떄문
dp = [[float('inf')] * (int((2 * N)** 0.5) + 1) for _ in range(N + 1)]
# dp[i][v]로 구성하여 도착지인 i번째 돌에 v의 속도로 도착하는 경우의 수 중 최소 점프 횟수를 value로 저장
dp[1][0] = 0
stone_set = set()
# 못가는 돌 넣기
for _ in range(M):
    stone_set.add(int(input()))

for i in range(2, N + 1):
    # 두번째 돌부터 못가는 돌인지 판단
    if i in stone_set:
        continue
    # 갈수있는 돌이면
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
# 이 점화식은 i라는 점에 j의 속도로 도달했을 때의 최소 점프횟수는 i - j의 위치에 
# 각각 j - 1, j, j + 1의 속도로 도달했을 떄의 최소 점프횟수 + 1이라는 뜻이다.
# j - 1, j, j + 1의 속도에서 각각 +1, +0, -1을 했을 때 j만큼 점프할 수 있기 때문에
# i - j에서 i로 갈 수 있기 때문이다.
if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))