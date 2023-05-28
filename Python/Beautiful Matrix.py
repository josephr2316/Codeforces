# 	263A - Beautiful Matrix
matrix = []
col_index = 0;
raw_index = 0;
cost = 0

# for i in range(5):
#     a.append([*map(int, input().split())])

for i in range (5):
    lst = [int(x) for x in input().split()]
    matrix.append(lst)
for x in range(5):
    for y in range(5):
        if matrix[x][y] == 1:
            col_index = y
            raw_index = x
# if col_index > 2:
#     cost = (col_index-2)
# else:
#     cost = cost + (2-col_index)
# if raw_index > 2:
#     cost += (raw_index-2)
# else:
#     cost +=  (2-raw_index)
cost = abs(col_index - 2) + abs(raw_index - 2) 
print(cost)
