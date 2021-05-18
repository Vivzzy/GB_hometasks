def int_func(vvod):
    res = str()
    for i in vvod:
        res += i.capitalize() + " "
    return res[:-1]


vvod = input().split()
print(int_func(vvod))
