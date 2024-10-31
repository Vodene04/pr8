def is_integer(n):
    try:
        float_n = float(n)
        return float_n.is_integer()
    except ValueError:
        return False
a = input("Введите первое число: ")
b = input("Введите второе число: ")
#Проверка на числа
if is_integer(a) and is_integer(b):
    a = int(a)
    b = int(b)
    start = min(a, b) + 1
    end = max(a, b)
    for number in range(start, end):
        print(number)
else:
    print("Ошибка! Числа должны быть целыми.")