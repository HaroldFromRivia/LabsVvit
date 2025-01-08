def greet(name):
    print("Здравствуй,", name)

def square(number):
    return number**2

def max_of_two(x, y):
    return max(x,y)

greet(input("Введите имя:"))
print(square(int(input("Введите число:"))))
print(max_of_two(int(input("Введите первое число:")),int(input("Введите второе число:"))))