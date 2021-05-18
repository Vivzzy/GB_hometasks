class Road():
    def count(self, length, width):
        _length = int(length)
        _width = int(width)
        print("Нужно", _length * _width * 25 * 0.05 / 1000, "тонн асфальта")


a = Road()
a.count(20000,5)