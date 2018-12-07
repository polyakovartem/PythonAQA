class Number:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def plus(self, other):
        sum = self.get_value() + other.get_value()
        return Number(sum)

    def __str__(self):
        return str(self.get_value())


class ComplexNumber(Number):
    def __init__(self, real, imaginary):
        Number.__init__(self, real)
        self.imaginary = imaginary

    def get_imaginary(self):
        return self.imaginary

    def plus(self, other):
        real_sum = self.get_value() + other.get_value()
        imaginary_sum = self.get_imaginary() + other.get_imaginary()
        return ComplexNumber(real_sum, imaginary_sum)

    def __str__(self):
        real = self.get_value()
        img = self.get_imaginary()
        return "{0} + {1}*i".format(real, img)


a = Number(2)
b = Number(3)
c = ComplexNumber(4, 2)
d = ComplexNumber(6, 7)

print(a.plus(b))  # 5 good
print(c.plus(d))  # 10 +9*i also good
print(b.plus(c))  # 7 is wrong, should be 7 + 2*i