import copy
matrix = [[1, 3, 5],
          [2, 4, 6]]

def transpose(matrix):
    matrixT = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrixT[y][x] = matrix[x][y]
    return matrixT

print(transpose(matrix))