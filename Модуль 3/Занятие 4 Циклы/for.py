# в итоговую строку добавлять только четные числа
result = ""
max = int(input("Введите число: "))
for i in range(0, max, 25):
        result = result + str(i) + " "
print(result)
