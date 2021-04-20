n = int(input("Введите целое положительное число: "))
l = []
while n > 0:
    l.append(n % 10)
    n = n // 10
print(max(l))
