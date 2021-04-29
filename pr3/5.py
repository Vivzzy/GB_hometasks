res = 0
flag = True
while flag:
    vvod = input("Введите строку чисел, * заканчивает программу:").split()
    for i in vvod:
        if i != "*":
            res += int(i)
        else:
            flag = False
            break
    print(res)
