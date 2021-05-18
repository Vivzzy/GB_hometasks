rating = [7, 5, 3, 3, 2]
rating.append(int(input("Введите ваше число: ")))
print("Текущий рейтинг:", str(sorted(rating, reverse=True))[1:-1], end='.')
