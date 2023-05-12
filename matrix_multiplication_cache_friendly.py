import numpy as np

def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = matrix1.shape
    rows2, cols2 = matrix2.shape

    if cols1 != rows2:
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    result = np.zeros((rows1, cols2), dtype=int)

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i, j] += matrix1[i, k] * matrix2[k, j]

    return result
