a = int(input("Введите а:"))
b = int(input("Введите b:"))
if a>b:
    print(a больше b)
elif a<b:
    print(a меньше b)
else:
    print(a равно b)


nums = [int(x) for x in input("Введите числа через пробел:"). split()]
sum_even = 0
sum_odd = 0

for n in nums:
    if n % 2 ==0:
        sum_even += n
    else:
        sum_odd += n
print("Сумма чётных:", sum_even)
print("Сумма нечётных:", sum_odd) 

numbers = [5, 3, 8, 6, 2, 8, 3]
unique_nums = list(set(numbers))
unique_nums = nums.sort(reverse=True)

if len(unique_nums) >= 2:
    print("Второе по величине число:", unique_nums[1])
else:
    print("Нет второго по величине числа")    





n = int(input("Введите n (положительное целое):"))
nums = list(range(1, n+1))

for x in nums:
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)




    numbers = [3, 7, 1, 9, 4]
    max_num = numbers[0]
    
    for n in numbers:
        if n > max_num:
            max_num = n
    print("Максимум:", max_num)



nums = []
for i in range(5):
    x = int(input("Введите число:"))
    nums.append(x)


total = 0

for n in nums:
    total += n


print("Сумма:", total)




names = ["Анна", "Борис", "Катя", "Дима"]


for name in names:
    if names.startswith("К"):
        print(name)








n = int(input("Ведите n:"))

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i)






n = int(input("Ведите n:"))
fact = 1

for i in range(1, n+1):
    fact*= |

print("Факториал:", fact)








data = input("Ведите числа через пробел:").split()
nums = [int(x) for x in data]
avg = sum(nums)/len(nums)
result = []

for n in nums:
    if n > avg:
        result.append(n)

print("Числс больше среднего:", result)







words = ["apple", "banana", "cherry", "date"]
upper_words = []

for w in words:
    upper_words.append(w.upper())

print(upper_words)






n = int(input("Введите n:"))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i}*{j}={i*j}", end="\t")
        print()




nums = [int(x) for x in input("Введите числа через пробел:").split()]
count = 0

for i in range(1, len(nums)):
    if nums[i]>nums[i-1]:
        count += 1

print("Количество элементов больше предыдущего:", count)





nums = [5, 2, 3, 2, 5, 2]

while 2 in nums:
    nums.remove(2)

print(nums)




words = input("Введите слова через пробел:").split()
longest = words[0]

for w in words:
    if len(w) > len(longest):
        longest = w

print("Самое длинное слово:", longest)
