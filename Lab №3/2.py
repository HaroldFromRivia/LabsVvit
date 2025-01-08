with open('user_input.txt', 'a') as file:
    file.write(input('Введите текст:'))
def readfunc(choice):
    if choice == 1:
        with open('example.txt', 'r') as file:
            content = file.read()
        print(content)
    elif choice == 2:
        with open('example.txt', 'r') as file:
            for line in file:
                print(line)
    else:
        print("Error")
readfunc(int(input("Выберите тип чтения:\n1.Чтение всего файла.\n2.Построчное чтение.\n")))
