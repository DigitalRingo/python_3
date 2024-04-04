
first_str = input("Введите первую строку:")
second_str = input("Введиите вторую строкку:")
first_str = first_str.upper()
second_str = second_str.upper()
print(f"Первая строка:{first_str};\nВторая строка:{second_str}")
if first_str.find(second_str) != -1:
    print("Есть контакт!")
else:
    print("Мимо!")