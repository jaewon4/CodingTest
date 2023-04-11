x, y, w, h = map(int, input().split())

compare_list = [x, y, w - x, h - y]

print(min(compare_list))



