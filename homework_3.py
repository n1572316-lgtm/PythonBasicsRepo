#1
m: int = int(input("Введите m"))
n: int = int(input("Введите n"))


for i in range(m, n+1):
    if i % 17==0 or (i % 3==0 and i % 5==0) or i % 10==9:
        print(i)



#2
n: int = int(input("Ведите число"))
for i in range(1, n+1):
    if 5<=i<=9 or 17<=i<=37 or 78<=i<=87:
        continue
    print(i)



#3
n: int = int(input("Введите число"))
j = 0
while j<=n-1:
    j+=1
    for i in range(1, 4):
        print(n, end="")
    print()

    