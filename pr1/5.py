earns = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
if earns > costs:
    print("Фирма прибыльна")
    print("Рентабельность выручки равна ", (earns - costs) / earns)
    staff = int(input("Введите количество сотрудников: "))
    print("Прибыль фирмы в расчете на одного сотрудника равна ", (earns - costs) / staff)
elif earns == costs:
    print("Фирма не имеет ни прибыли, ни убытков")
else:
    print("Фирма убыточна")
