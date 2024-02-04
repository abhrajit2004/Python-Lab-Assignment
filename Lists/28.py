x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

rows_x = len(x)
cols_x = len(x[0])

rows_y = len(y)
cols_y = len(y[0])

if cols_x != rows_y:
    print("The matrices cannot be multiplied")
    exit()

result = [[0 for j in range(cols_y)]for i in range(rows_x)]

for i in range(rows_x):
    for j in range(cols_y):
        for k in range(rows_y):
            result[i][j] += x[i][k] * y[k][j]

print(result)