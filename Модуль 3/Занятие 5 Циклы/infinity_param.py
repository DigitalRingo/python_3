# Бесконечный цикл while
a = True
magic_number = 7
print("Угадайте загаданное число:)")
while a:
    input_value = input("Введите число:")
    if input_value == "выход":
        break
    number = int(input_value)
    print("Значение number: ", number)
    if magic_number == number:
        print("Поздравляем! Вы угадали загаданное число!")
        a = False

print("Программа завершена")