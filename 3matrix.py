def matrix_input(rows, columns):
    m = [[0] * columns for r_i in range(rows)]

    for r_i in range(rows):
        for c_i in range(columns):
            m[r_i][c_i] = int(input())
    return m


def matrix_print(m):
    for r_i in range(rows):
        for c_i in range(columns):
            print(m[r_i][c_i], end=" ")
        print()


while True:
    try:
        rows = int(input("Введите кол-во строк "))
        columns = int(input("Введите кол-во столбцов "))
        matrix = matrix_input(rows, columns)
        break
    except TypeError:
        print("Ошибка. Введите целое число")

matrix_print(matrix)

fl = 1
j = 0
sum_columns = 0

for j in range(columns):
    for i in range(rows):
        if matrix[i][j] >= 0:
            fl = 0
    if fl:
        for i in range(rows):
            sum_columns += matrix[i][j]
        break

if fl:
    print("Сумма отрицательных элементов столца", sum_columns, "\nСреднее арифмитическое", sum_columns / rows)
else:
    print("Столбец с отрицательными членами отсутсвует")
