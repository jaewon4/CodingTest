import sys
input = sys.stdin.readline

num_list = list()

for _ in range(9):
    num_list.append(int(input()))

max_val = max(num_list)
index = num_list.index(max_val) + 1

print(max_val)
print(index)


