try:
    def readfunc(choice):
        if choice == 1:
                with open('dheuwifwe.txt', 'r') as file:
                    content = file.read()
                print(content)
        elif choice == 2:
            with open('example.txt', 'r') as file:
                for line in file:
                    print(line)
        else:
            print("Error")
except FileNotFoundError:
    print('fmnnrge')
readfunc(int(input("Выберите тип чтения:\n1.Чтение всего файла.\n2.Построчное чтение.\n")))
