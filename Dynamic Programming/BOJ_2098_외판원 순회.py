import sys
sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK04/input.txt", "rt")
input = sys.stdin.readline
N = int(input()) # 4
W = []
for i in range(N):
    W.append([])
    W[i] = list(map(int, input().split()))
dp = [[0 for j in range(1 << 16)] for i in range(16)]

def tsp(c,v): # v는 방문한 모든 도시 리스트, 2진수로 작성 
    if v == (1<<N)-1: # v == 15 1111 즉 모든 도시를 방문했다면,
        if W[c][0] == 0: # 시작 도시로 돌아갈 수 없을 때
            return float('inf')
        else:
            return W[c][0]
        
    if dp[c][v] != 0:
        return dp[c][v]
    
    min_val = float('inf')
    for i in range(0, N): # 0 1 2 3
        if (v & (1<<i)) == 0 and W[c][i] != 0: # 방문한 적이 없고, 갈 수 있는 도시일 때 
            min_val = min(min_val, tsp(i, (v | (1 << i))) + W[c][i])
    dp[c][v] = min_val
    return dp[c][v]

print(tsp(0,1))