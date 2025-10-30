# file = open('smth.txt','r')
# print(file.read())
# file.close()
# try:
#     with open('smth.txt', 'r', encoding='utf-8') as file:
#         print(file.read())
#         # print(file.readlines())
#         # txt = file.readlines()
#         # print(txt[-1])
# except:
#     print('File not found')

# with open('smth.txt', 'w') as file:
#     file.write('Pythin')
#     file.write('------')
#     print('Запис до файлу виконано')


# f1="smth.txt"
# f2="sm1.txt"
# with open(f1, encoding='utf-8') as inFile:
#     fileContents = inFile.read()
#     fileContents=fileContents.upper()
#     with open(f2, 'a') as outFile:
#         outFile.write(fileContents)
#     print('Все виконано')

# with open("smth.txt", 'w') as f:
#     f.write("Hello World")
#     print('yes')

# with open('smth.txt', 'r') as f:
#     text = f.read()
#     with open('sm1.txt', 'w') as f2:
#         f2.write(text)
#     print("complete")

# try:
#     with open('smth.txt', 'r') as f:
#         print(len(f.readlines()))
# except FileNotFoundError:
#     print('File not found')

# try:
#     with open('smth.txt', 'r') as f:
#         f2 = f.read()
#         f3 = f2.split()
#         f4 = f2.splitlines()
#         print(f'Кількість слів: {len(f3)}')
#         print(f"Кількість символів: {len(f2)}")
#         print(f"Кількість рядків: {len(f4)}")
# except:
#     print("Функцію не виконано")


# with open("smth2.txt", 'w', encoding="utf-8") as f:
#     while True:
#         x = input("Введіть рядок: ")
#         if x == "":
#             break

import string

alphabet="АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
exeptions=[string.digits, string.ascii_letters, " "]

try:
    with open("sm1.txt", "r", encoding="utf-8") as f:
        res=""
        text = f.read().upper()
        for el in range(len(text)):
            print(el, text[el])
            sym=text[el]
            if sym not in exeptions:
                res += alphabet[alphabet.find(sym)+1]

    with open("encrypted.txt", "w", encoding="utf-8") as f:
        f.write(res)
except FileNotFoundError:
    raise "Файл не знайдено!"


