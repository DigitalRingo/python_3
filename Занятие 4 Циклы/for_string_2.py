# заменить заданный символ в строке на символ "*"
string = input("Введите строку: ")
symbol = input("Введите символ: ")
result = ""
for s in string:
    if s == symbol:
        result = result + "*"
    else:
        result = result + s
print(result)
