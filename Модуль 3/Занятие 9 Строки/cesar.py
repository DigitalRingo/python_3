#шифр Цезаря (сдвиг на один символ вправо)
# абвг -> бвгд
# слово -> тмпгп
alphabet = 'абвгдеёжзийклмнопрстуфцчшщъыьэюя'
message = input("Введите текст для шифрования:")
encrypted_message = ""
for i in message:
    if alphabet.find(i) > -1:
        current_index = alphabet.index(i)
        new_index = (current_index + 1) % len(alphabet)
        print("new index:", new_index)
        encrypted_message = encrypted_message + alphabet[new_index]
    else:
        encrypted_message = encrypted_message + i
print("Зашифрованный текст:", encrypted_message)
