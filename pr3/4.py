def my_func(x, y):
    for i in range(abs(y) - 1):
        x *= x
    return 1 / x


x, y = map(int, input("Введите x и y через пробел: ").split())
print(my_func(x, y))
