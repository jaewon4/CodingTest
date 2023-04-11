def hanoi(n, start, mid, end):
    if n == 1:
        print(f"{start} {end}")
        return
    hanoi(n-1, start, end, mid)
    print(f"{start} {end}")
    hanoi(n-1, mid, start, end)


disk_cnt = int(input())
print(2 ** disk_cnt- 1)

if disk_cnt <= 20:
    hanoi(disk_cnt, 1, 2, 3)
else:
    pass





# def 하노이탑(원판개수, 시작기둥, 보조기둥, 대상기둥):
#     if 원판개수 == 1:
#         print(f"{시작기둥} {대상기둥}")
#     else:
#         하노이탑(원판개수 - 1, 시작기둥, 대상기둥, 보조기둥)
#         print(f"{시작기둥} {대상기둥}")
#         하노이탑(원판개수 -1, 보조기둥, 시작기둥, 대상기둥)

# 원판개수 = int(input())
# print(2 ** 원판개수- 1)

# if 원판개수 <= 20:
#     하노이탑(원판개수, 1, 2, 3)
# else:
#     pass

