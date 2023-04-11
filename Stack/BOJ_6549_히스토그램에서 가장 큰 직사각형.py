# 6549번 히스토그램에서 가장 큰 직사각형
import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")

while True:
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)

    if n == 0:
        break

    stack = []
    answer = 0

    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        # 스택에 데이터가 있으면서 
        # rec의 i번째 기둥의 길이보다 스택에있는 rec[stack[-1]]의 기둥이 크다면
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            # 넓이를 계산하려고 pop
            tmp = stack.pop()
            # 스택이 비어있으면
            if len(stack) == 0:
                width = i
            # 스택에 데이터가 있으면
            else:
                # i는 right 이라고 생각
                # stack[-1]은 left라고 생각하기
                width = i - stack[-1] - 1
            # 최대값을 추적하기위한 max함수
            answer = max(answer, width * rec[tmp])
        # rec의 i번째 기둥의 길이보다 스택에있는 rec[stack[-1]]의 기둥이 작다면
        stack.append(i)

    # 스택에 남아있는 것을 처리
    while len(stack) != 0:
        tmp = stack.pop()

        if len(stack) == 0:
            # n은 전체 폭이므로
            width = n
        else:
            # 전체폭 - stack[-1]의 값 -1로 폭을 구할수 있다. 
            width = n - stack[-1] - 1
        answer = max(answer, width * rec[tmp])

    print(answer)