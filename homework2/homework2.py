while True:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
 #Проверка на то, является ли введенное значение целым числом
    if a.replace("-", "").isdigit() and b.replace("-", "").isdigit():
        a1 = int(a)
        b2 = int(b)
        sum = a1 + b2
        print(f"Сумма чисел равна: {sum}")
    else:
        print("Ошибка ввода данных.")