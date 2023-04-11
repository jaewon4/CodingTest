x, y = map(int, input().split())
row = [0]
column = [0]
row.append(x)
column.append(y)

for _ in range(int(input())):
    identifier, length = map(int, input().split())
    if identifier == 1:
        row.append(length)
    else:
        column.append(length)

row.sort()
column.sort()

split_row = []
split_col = []

for i in range(len(row) - 1):
    split_row.append(row[i+1] - row[i])

for i in range(len(column) - 1):
    split_col.append(column[i+1] - column[i])

print(max(split_row) * max(split_col))


# paper_width, paper_height = map(int, input().split())
# #자르는 위치 저장
# row = [0, paper_width]    # [0, 10]
# column = [0, paper_height] #  [0, 8] 

# for _ in range(int(input())):   # 자르는 횟수
#     identifier, linenumber = map(int, input().split())  
#     if identifier == 1:             # 세로가 1 가로가 0-> 세로는 r에 가로는 paper_height 
#         row.append(linenumber)
#     else :
#         column.append(linenumber)

# row.sort()     # [0, 4, 10]
# column.sort()  # [0, 2, 3, 8]
#                # 빼서 최대 길이 구하기

# subtracted_width = []  #[4, 6]
# subtracted_height = []  #[2, 1, 5]

# for i in range(len(row)-1):    # 0 1
#     subtracted_width.append(row[i + 1] - row[i])   # row[1]-row[0]   row[2]-row[1]
# for i in range(len(column) -1): # 0 1 2 
#     subtracted_height.append(column[i+1]- column[i]) #col[1]-col[0]  col[2]-col[1]  col[3]-col[2]

# print(max(subtracted_width) * max(subtracted_height))