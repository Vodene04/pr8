def is_number(value):
    return value.lstrip('-').replace('.', '', 1).isdigit()
#Итоговая сумма
total_sum = 0.0

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения ввода): ")
    if user_input.lower() in ['stop', 'end']:
        break
    if not is_number(user_input):
        print("Ошибка: введено некорректное значение. Пожалуйста, попробуйте снова.")
        continue
    total_sum += float(user_input)
print(f"Сумма введённых чисел: {total_sum}")