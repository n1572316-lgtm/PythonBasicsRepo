p = int(input("Введите количество строк(n):"))
m = int(input("Ведите количество столбцов (m):"))

matrix = []
print("Введите элементы матрицы построчно:")
for i in range(p):
    row = list(map(int, input(f"Строка{i+1}:").split()))
    matrix.append(row)

transposed_matrix = []
for j in range(m):
    new_row = []
    for i in range(p):
        new_row.append(matrix[i][j])
    transposed_matrix.append(new_row)

print("\n Транспонированная матрица:")
for row in transposed_matrix:
    for element in row:
        print(f"{element:4d}", end="")# Форматирование выравнивания элементов
    print()