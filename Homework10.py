#Ex1
import random

def get_matrix():
    matrix = []

    for i in range(10):
        row = []
        for j in range(10):
            row.append(random.randint(-50, 200))  # генерируем случайное число от -50 до 200
        matrix.append(row)

    return matrix

matrix1 = get_matrix()
matrix2 = get_matrix()

matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(10)] for i in range(10)]

print(matrix1)
print(matrix2)
print(matrix3)
