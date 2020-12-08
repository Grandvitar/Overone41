try:
    number = input("Введите число: ")
    if not number.isnumeric():
        raise ValueError
except ValueError:
    print("Введены некорректные данные")
print("Cheking Git functions")
print("Cheking Git branches")
print("Cheking Git branches one more time")
