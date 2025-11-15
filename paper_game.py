import random

figures: list[str] = ["камень", "ножницы", "бумага"]
                      
while True:
    u_c: str = input("Введите фигуру: ")
    c_c: str = random.choice(figures)

    print("Выбор компа:", c_c)

    if (u_c =="камень" and c_c =="ножницы")\
        or (u_c =="ножницы" and c_c == "бумага")\
        or (u_c == "бумага" and c_c == "камень"):
        print("WIN!!!") 
    elif u_c == c_c:
        print("TIE!!!")
    elif u_c not in figures:
        print("Figure missmatch!!!")
    else:
        print("LOOSE!!!")

    user_break: str = input("Du u wanna continue? (y/n):")

    if user_break == "n":
        break
    elif user_break not in ["y", "n"]:
         print("I don't understand!") 