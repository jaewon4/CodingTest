n, k=map(int, input().split())
levels=[]

for _ in range(n):  
    levels.append(int(input()))

start = min(levels)
end = min(levels)+k
ans = 0
while start <= end:
    mid = (start+end)//2
    hap = 0
    for level in levels:
        if level < mid:
            hap = hap + (mid-level)

    if hap <= k:
        ans = max(mid,ans)
        start = mid + 1
    else:
        end = mid - 1


print(ans)