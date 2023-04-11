t = int(input())
for i in range(t):
    num, s = input().split()
    text = str()
    # 텍스트도 곱해진다.
    for i in s:
        text += int(num) * i
    print(text)


# n = int(input())

# for _ in range(n):
#     input_val = input()
#     split_val = input_val.split()
#     counter = int(split_val[0])
#     string = split_val[1]
#     string_list = list(string)
#     result = str()

#     for spell in string_list:
#         result += (spell * counter)
#         print(result)
#     print(result)
