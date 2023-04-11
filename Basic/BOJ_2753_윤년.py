input_year = int(input())

if input_year % 4 == 0 and input_year % 100 != 0:
    print("1")
elif input_year % 400 == 0:
    print("1")
else:
    print("0")
