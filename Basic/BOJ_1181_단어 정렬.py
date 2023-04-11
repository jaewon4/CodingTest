import sys

input = sys.stdin.readline
word_cnt = int(input())
word_list = []

for _ in range(word_cnt):
    word_list.append(input().rstrip())

# 중복값 제거
word_list = list(set(word_list))

word_list.sort(key= lambda x: (len(x), x))

for word in word_list:
    print(word)