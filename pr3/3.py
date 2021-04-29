def my_func(x, y, z):
    return x + y + z - min(x, y, z)


x, y, z = map(int, input("Введите x,y и z через пробел: ").split())
print(my_func(x, y, z))
