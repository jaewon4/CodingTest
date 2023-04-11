num1, num2 = input().split()
print(num1)
print(num1[::-1])
num1 = int(num1[::-1])
num2 = int(num2[::-1])

print(num1) if num1 > num2 else print(num2)


# a = list(num1)
# b = list(num2)
# a.reverse()
# b.reverse()

# x = int("".join(a))
# y = int("".join(b))

# if x > y:
#     print(x)
# else:
#     print(y)

