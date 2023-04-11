a,b,v = map(int,input().split())
# 앞부분은 마지막 부분에 내려가는 부분을 고려한 변수이다.
# 뒷부분은 순수 하루 이동량을 나타낸다.
k = (v-b)/(a-b)

# **** 이 조건문이 핵심임 *******
# print(int(k) if k == int(k) else int(k)+1)

if k == int(k):
    print(int(k))
else:
    print(int(k) + 1)


