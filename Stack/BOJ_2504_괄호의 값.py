import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")
bracket = sys.stdin.readline().rstrip()

stack = []
isAns = True
tmp = 1
ans = 0

for i, str in enumerate(bracket):
    # 스택에 '('를 넣으면 tmp * 2
    if str == "(":
        stack.append(str)
        tmp *= 2
    # 스택에 '['를 넣으면 tmp * 3
    elif str == "[":
        stack.append(str)
        tmp *= 3
    # 스택에 ')'를 넣으면 tmp //= 2를 하면서 ans에 더하면서 저장
    elif str == ")":
        if not stack or stack[- 1] == "[":
            isAns = False
            break
        if bracket[i-1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2
    # 스택에 ']'를 넣으면 tmp //= 3 하면서 ans에 더하면서 저장
    elif str == "]":
        if not stack or stack[- 1] == "(":
            isAns = False
            break
        if bracket[i-1] == "[":
            ans += tmp
        stack.pop()
        tmp //= 3

if not isAns or stack:
    print(0)
else:
    print(ans)