def division(x, y):
    if y != 0:
        res = x / y
    else:
        res = "Делить на ноль плохо"
    return res


x = int(input("Введите делимое: "))
y = int(input("Введите делитель: "))
print(division(x, y))
