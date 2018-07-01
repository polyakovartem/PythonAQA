class Mai:
    high = 47
    con = 10
    def __init__ (self, a : int = 0, b : int = 100, sums : int = 3) -> None:
        self.a = a
        self.b = b
        self._sums = sums
        self.__sums3 = sums*sums
    def adder (self, x : int) -> float:
        self.x = x
        x = ((x * self.b) - self.a) * 1.2
        return x
    def prints(self) -> None:
        print(self.a, self.b, self._sums, self.__sums3)

class Mo(Mai):
    con = 11
    def adder (self, x :int) -> float:
        self.x = x
        x = ((x * self.b) - self.a) * 1.4
        return x

