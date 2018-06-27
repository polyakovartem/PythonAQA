import abc as models
import math

# SRP Принцип единственной ответственности (The Single Responsibility Principle)
class TV(object):
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def getName(self):
        return self._name()

    def getColor(self):
        return self._color.get()

    def getMaxSize(self):
        return self._size


class TVOn(object):
    def __init__(self, TV, state):
        self._state = state
        self._TV = TV


class TVSwitch(object):
    def __init__(self, TV, state):
        self._state = state
        self._TV = TV

    def print(self):
        return print('TV: {}, Max Size: {}, Color: {}'.format(self._TV.getName(), self._TV.getMaxSize(), self._TV.get()))

# OCP Принцип открытости/закрытости (The Open Closed Principle)

class User(UnknownUser):
    bio = models.TextField(max_length = 1000, blank = True)
    location = models.CharField(max_length = 50, blank = True)
    birth_date = models.DateField(null = True, blank = True)

# LSP Принцип подстановки Барбары Лисков (The Liskov Substitution Principle)
class TV(object):

    def getWidth(self):
        return width

    def setWidth(self, width):
        self._width = width

    def getHeight(self):
        return height

    def setHeight(self, height):
        self._height = height

    def calculateDiagonal(self):
        return math.sqrt(pow(self._width, 2) * pow(self._height, 2))


class Monitor(TV):
    def setWidth(self, width):
        self._width = width
        self._height = height

class TestTV(unittest.TestCase):

    def setUp(self):
        pass

    def test_calculateDiagonal(self):
        a = TV()
        a.setWidth(5);
        a.setHeight(4);
        self.assertEqual(a.calculateDiagonal(), 20)


#      ISP Принцип разделения интерфейса (The Interface Segregation Principle)
class Car(models.ABC):
    @models.abstractmethod
    def man(self) -> str:
        pass


class Carman(Car):
    def man(self) -> str:
        return 'string'


def OXL(object: Car):
    object.man()


# DIP Принцип инверсии зависимостей (The Dependency Inversion Principle)
class Engine(object):
    def __init__(self):
        pass

    def accelerate(self):
        pass

    def getRPM(self):
        currentRPM = 0
        return currentRPM


class Vehicle(object):
    def __init__(self):
        self._engine = Engine()

    def getEngineRPM(self):
        return self._engine.getRPM()

