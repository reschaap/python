def matrixElementsSum(matrix):
    del_index = []
    matrix_sum = 0
    for row in (matrix):
        for i in del_index:
            row[i] = 0
        for index, value in enumerate(row):
            if value == 0:
                del_index.append(index)
            else:
                matrix_sum += value
    return matrix_sum


#client
matrix_1 = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrix_2 = [[1,1,1,0],
 [0,5,0,1],
 [2,1,3,10]]

print(matrixElementsSum(matrix_1))
print(matrixElementsSum(matrix_2))