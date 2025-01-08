
def readfunc(choice):
    if choice == 1:
        try:
            with open('wrongfile.txt', 'r') as file:
                content = file.read()
            print(content)
        except FileNotFoundError:
            print('Такого файла не существует.')
    elif choice == 2:
        with open('example.txt', 'r') as file:
            for line in file:
                print(line)
    else:
        print("Error")


readfunc(int(input("Выберите тип чтения:\n1.Чтение всего файла.\n2.Построчное чтение.\n")))
