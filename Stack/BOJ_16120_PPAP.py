import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK03/input.txt", "rt")
input = sys.stdin.readline
string_list = list(input().rstrip())
stack = []

for string in string_list:
    stack.append(string)
    sum1 = ''.join(stack[-4:])
    if sum1 == 'PPAP':
        del stack[-3:]

sum2 = ''.join(stack)

if sum2 == 'P':
    print('PPAP')
else:
    print('NP')