input_in_sec = int(input("Введите время в секундах: "))
hour = (input_in_sec // 3600) % 24
minutes = (input_in_sec // 60) % 60
seconds = input_in_sec % 60
print("{:d}:{:d}:{:d}".format(hour, minutes, seconds))
