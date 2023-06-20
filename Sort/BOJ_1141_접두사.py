import sys
sys.stdin=open("/Users/admin/Documents/swjungle_PS/jaewon/푸는중/input.txt", "rt")
input = sys.stdin.readline

n = int(input())
s_list = []
for _ in range(n):
    s_list.append(input().rstrip())
s_list.sort(key=len)

count = n
for i in range(len(s_list)):
    for j in range(i + 1, len(s_list)):
        if s_list[j].startswith(s_list[i]):
            count -= 1
            break
print(count)



# import sys
# input = sys.stdin.readline
# n = int(input())

# jubdu = list([] for _ in range(n))
# word_list = []
# for _ in range(n):
#     word_list.append((input().strip()))
# word_list.sort()

# for i in range(n):
#     m = len(word_list[i])
#     for j in range(i+1, n):
#         if word_list[i] == word_list[j][:m]:
#             jubdu[i].append(j)
#         else:
#             break

# real_list = []  

# for idx in range(len(word_list)-1, -1, -1):
#     if not word_list[idx]:
#         real_list.append(idx)

#     else:
#         for iz in jubdu[idx]:
#             if iz in real_list:
#                 break
#         else:
#             real_list.append(idx)

# print(len(real_list))




