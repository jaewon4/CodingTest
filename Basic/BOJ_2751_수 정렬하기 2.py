import sys
# input()은 sys.stdin.readline.rstrip()과 같다!! 근데 더빠르다!
n = int(sys.stdin.readline().rstrip())
num_list = list()

for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()

for i in num_list:
    print(i)