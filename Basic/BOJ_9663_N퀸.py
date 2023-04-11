n = int(input())
ans = 0
pos = [0] * n

def is_promising(x):
    for i in range(x):
        if pos[x] == pos[i] or abs(pos[x] - pos[i]) == abs(x - i):
            return False
    return True

def dfs(depth):
    global ans
    if depth == n:
        ans += 1
        return
    else:
        for i in range(n):
            # pos[depth]의 의미는 x번째 리스트의 값을 정하는것인데
            # 이 값은 어떤 열(row)인지를 나타낸다.
            # pos[0] = 0 => [0, 0, 0, 0]에서 첫번쨰 체스를 0번째줄에 둔다는 의미
            # pos[0] = 1 => [1, 0, 0, 0]은 체스를 1번째줄에 둔다는 의미
            # pos[1] = 3 => [?, 3, 0, 0]은 체스를 3번쨰줄에 둔다는 의미
            pos[depth] = i
            if is_promising(depth):
                dfs(depth + 1)

dfs(0)
print(ans)


# col[i] : i번째 행(row)에서 퀸이 놓여있는 열(col)의 위치
# col[k] : k번째 행(row)에서 퀸이 놓여있는 열(col)의 위치

# 같은 열 체크
# col[i] == col[k] : 같은 열에 놓이게 되므로 유망하지 않다.
# 대각선 체크
# col[i] - col[k] == abs(i - k)
# col[i] - col[k] == abs(k - i)