from collections import deque
import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input=sys.stdin.readline

n, k = map(int, input().split())
coins=list(int(input()) for _ in range(n))
# k+1까지 배열을 만들어 합쳐지는 값이 k에 있는 인덱스와 같다면 체크를 해준다.
check=[0 for _ in range(k+1)]

def bfs(coins, k):
    queue=deque()

    for coin in coins:
        # 코인이 k보다 크면 안됨
        if coin < k:
            # 하나의 코인을 이용하여 첫 que를 넣는다. 즉, 초기값 셋팅
            queue.append([coin, 1])
            # 체크표시
            check[coin] = 1

    while queue:
        # 축척된 코인값, 사용된 코인 개수
        cum, cnt=queue.popleft()
        # 만약 축척된 코인값이 목표 k값이면 탈출
        if k == cum:
            print(cnt)
            break
        for coin in coins:
            # 큐에 있던 코인에 가능한 코인 전부를 더해본다.
            # 그리고 개수를 증가시킨다. 더하니까
            cum1 = cum + coin
            cnt1 = cnt + 1
            # 만약 합친 값이 k보다크면 무시
            if cum1 > k:
                continue
            # 합친 값이 k보다 작거나 같고 그리고 check배열을 확인하여 같은 값을 만들어 큐에 넣은적이 없으면
            # check배열은 큐에 합친값을 넣어보았다면 check해주는 배열이다. 즉 (15, 3)이 이전에 check배열에 체크를 해줬다면
            # (15, 4)는 큐에 들어갈수 없다 왜냐하면 3개로 이미 만들었기에 넣을 필요가 없기때문이다. 그래서 check배열이 있다.
            elif cum1 <= k and check[cum1] == 0:
                check[cum1] = 1
                queue.append([cum1, cnt1])
            
    if cum!=k:
        print('-1')

bfs(coins,k)