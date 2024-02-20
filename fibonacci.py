# 0 1 1 2 3 5 8 13...
a = 0
b = 1
n = int(input("Введите n: "))
prefix = "Числа Фибоначчи: "
if n == 1:
    print(prefix, a)
elif n > 1:
    print(prefix, a, b, end=" ")

for i in range(2, n):
    current = a + b
    a = b
    b = current
    print(current, end=" ")

print("золотое сечение:", b / a)