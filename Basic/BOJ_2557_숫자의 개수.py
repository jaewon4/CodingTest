num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = list(str(num_1 * num_2 * num_3))

for i in range(10):
    # count쓰는게 핵심
    print(result.count(str(i)))
