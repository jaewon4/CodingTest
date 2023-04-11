a = input()
b = input()

split_a = list(a)
split_b = list(b)

# 원본이 바뀌게 된다.
split_b.reverse()

for i in split_b:
    print(int(a) * int(i))

print(int(a) * int(b))