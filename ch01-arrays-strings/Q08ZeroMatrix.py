from typing import List

def ZeroMatrix(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    rows, cols = [], []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for row in rows:
        nullifyRow(matrix, row)

    for col in cols:
        nullifyCol(matrix, col)
    
    return matrix

def nullifyRow(matrix, row):
    for col in range(len(matrix[0])):
        matrix[row][col] = 0         

def nullifyCol(matrix, col):
    for row in range(len(matrix)):
        matrix[row][col] = 0

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

    print(ZeroMatrix(matrix))