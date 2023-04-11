import sys
# sys.stdin=open("/Users/admin/Documents/JUNGLE/WEEK02/input.txt", "rt")
input=sys.stdin.readline

n = int(input())
stack = [int(input()) for _ in range(n)]
count = 1
last = stack[-1]

for i in reversed(range(len(stack))):
      if stack[i] > last:
            count += 1
            last = stack[i]
            
print(count)