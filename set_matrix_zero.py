# def setZeroes(matrix):
#     rows = len(matrix)
#     columns = len(matrix[0])
#     zero_cols = set()
#     zero_rows = set()
#     for i in range(rows):
#         for j in range(columns):
#             if matrix[i][j] == 0:
#                 zero_cols.add(j)
#                 zero_rows.add(i)
    
#     for i in range(rows):
#         for j in range(columns):
#             if i in zero_rows or j in zero_cols:
#                 matrix[i][j] = 0

#     return matrix
                
                
# print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))






def setZeroes(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    changed = set()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0 and (i, j) not in changed:
                for k in range(rows):
                    matrix[i][k] = 0
                    changed.add((i, k))
                if columns != rows:
                    for k in range(columns - 1):
                        print(matrix[k][j])
                        matrix[k][j] = 0
                        changed.add((k, j))
                else:
                    for k in range(columns):
                        print(matrix[k][j])
                        matrix[k][j] = 0
                        changed.add((k, j))

    return matrix
                
                
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))