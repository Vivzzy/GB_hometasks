products = []
sample = {"название": 0, "цена": 0, "количество": 0, "ед": 0}
analytics = {"название": [], "цена": [], "количество": [], "ед": []}
i = 1
while True:
    temp_dict = sample
    for j in temp_dict.keys():
        temp = input("Введите {} товара: ".format(j))
        try:
            temp = int(temp)
        except ValueError:
            temp = temp
        temp_dict[j] = temp
        if temp not in analytics[j]:
            analytics[j].append(temp)
    products.append((i, temp_dict))
    i += 1
    if input("Введите Y, чтобы продолжить: ").upper() != "Y":
        break
print(products)
print(analytics)
