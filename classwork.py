# вывыести дни календаря с красивым форматированием
days = int(input("Введите количество дней в месяце: "))
month_start = int(input("Введите первый день месяца: "))

print("пн", "вт", "ср", "чт", "пт", "сб", "вс")
for i in range(0, month_start):
    print("   ", end="")
for i in range(1, days + 1):
    if (i // 10 > 0):
        separator = " "
    else:
        separator = "  "
    if (i + month_start) % 7 != 0:
        print(i, end=separator)
    else:
        print(i, end="\n")