s = "наша базовая строка"
sub = "а"

print(s)  # len(string) длина строки
print("длина строки", len(s))

# string.find(substring) Поиск подстроки в строке. Возвращает номер первого вхождения или -1
i = s.find(sub)
print("номер первого вхождения", i)

# string.rfind(substring) Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
print("номер последнего вхождения", s.rfind(sub))

# string.index(substring) Поиск подстроки в строке. Возвращает номер первого вхождения или ValueError
print("номер первого вхождения (индекс)", s.index(sub))

# string.rindex(substring) Поиск подстроки в строке. Возвращает номер последнего вхождения
print("номер последнего вхождения (индекс)", s.rindex(sub))

# string.split(sep) Разбиение строки по разделителю
print(s.split(" "))

# s.join(список) Сборка строки из списка с разделителем s
print("сборка строки с разделителем")
some_words = s.split(" ")
sep = "||"
print(sep.join(some_words))
print(sep.join("слово"))
print(sep.join(["слово"]))

# string.startswith(substring) Начинается ли строка string с шаблона substring
print("начинается ли строка с шаблона", s.startswith("наша "))

# string.endswith(substring) заканчивается ли строка string шаблоном substring
print("заканчивается ли строка шаблоном", s.endswith("строка"))

# string.strip() Удаление пробельных символов в начале и в конце строки
print("удаление пробельных символов в начале и конце")
print("     строка с пробелами по краям       ".strip())

# string.replace(шаблон, замена) Замена шаблона на замену. Можно удалить символы, если замена будет пустой строкой
print("замена шаблона на строку")
print(s.replace(" ", "_"))

# string.isdigit() состоит ли строка из цифрprint("состоит ли строка из цифр")
print("1234567".isdigit())

# string.isalpha() Состоит ли строка из буквprint("состоит ли строка из букв")
print("буквы".isalpha())

# string.isalnum()  # Состоит ли строка из цифр или буквprint("состоит ли строка из букв или цифр")
print("цифры 123", "цифры 123".isalnum())
print("цифры123", "цифры123".isalnum())
print("цифры", "цифры".isalnum())
print("123", "123".isalnum())
