# 이 문제는 형태를 외워두기!!!!!!!!!!!!!!!!!!!!!!
import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder(start, end):
    if start > end:
        return
    # end + 1을 해주는 이유는 for 문을 거치지 않고
    # postorder(div, end)에서 end와 div가 같으면 무한루프에 빠지기떄문임
    # 루트보다 큰 값이 존재하지 않을 경우를 대비 
    div = end + 1
    # start + 1 : 루트노드를 제외하고 비교를 하기떄문
    # end + 1 : 그래야 end까지의 인덱스가 i에 들어가 배열의 끝까지 돌수있다.
    # ref) range(n)는 n-1까지의 인덱스까지 방문한다.
    # 루트노드의 값이 비교할 노드의 값보다 작으면 div 갱신
    for i in range(start+1,end+1):
        if num_list[start] < num_list[i]:
            div = i
            break
    # 왼쪽
    postorder(start+1, div-1)
    # 오른쪽
    postorder(div, end)
    # 루트노드 체크(후위순회 결과출력)
    # print의 위치조정으로 전위, 중위, 후위순회를 나타낼수 있다.
    print(num_list[start])

postorder(0, len(num_list)-1)