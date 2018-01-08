from itertools import compress

def matrixElementsSum(matrix):
    mask = [1, 1, 1, 1]
    matrix_sum = 0
    for row in matrix:
        print("mask: {}".format(mask))
        print("row: {}".format(row))
        matrix_sum += sum(compress(row, mask))
        mask = create_mask(row, mask)
    return matrix_sum


def create_mask(row, mask):
    new_mask = []
    for index, number in enumerate(row):
        if number > 0 and mask[index] > 0:
            new_mask.append(1)
        else:
            new_mask.append(0)
    return new_mask



#client
matrix_1 = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrix_2 = [[1,1,1,0],
 [0,5,0,1],
 [2,1,3,10]]

print(matrixElementsSum(matrix_1))
print(matrixElementsSum(matrix_2))