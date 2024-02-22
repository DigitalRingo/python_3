# посчитать количество заданных символов в строке
string = input("Введите строку: ")
symbol = input("Введите символ: ")
count: int = 0
for s in string:
    if s == symbol:
        count = count + 1
print("Количество символов", symbol, ":", count)
