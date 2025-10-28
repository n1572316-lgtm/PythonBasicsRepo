# num: int = int(input())

# nums: list[int] = []

# for i in range(num):
#     nums.append(int(input()))


#     index: int = 0

#     while index < len(nums):
#         if nums[i] % 3 == 0 or nums[i] % 5 == 0:
#             nums.pop(i)
#         index += 1

#     for num in nums:
#         print(num, end="")


# print(nums)


# u_c: str = input("Введите фигуру")
# с_с: str = 

matrix: list[list[int]] = []

for i in range(1, 6):
    row: list[int] =[]
    for j in range(1, 6):
        row.append(i*5+j+1)
    matrix.append(row)

for row in matrix:
    print(row) 

diag_sum: int = 0

for i in range(len(matrix)):
    diag_sum += matrix[i][i]

print(diag_sum)

diag_sum_list: int = sum([matrix[i][i]] for i in range(len(matrix)))
print(diag_sum_list)
print()