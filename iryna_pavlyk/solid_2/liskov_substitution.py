"""
This module describes a homework related to SOLID.
Liskov Substitution principle
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{} {} makes noise: 'Some noise!'".format(Animal.__name__, self.name))

    def eat(self, food):
        print("{} {} likes eating {}".format(Animal.__name__, self.name, food))


class Duck(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print("{} {} makes noise: 'Duck-duck-duck!'".format(Duck.__name__, self.name))

    def eat(self, food):
        print("{} {} likes eating {}".format(Duck.__name__, self.name, food))


class Fish(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print("{} {} makes noise: 'Bul-bul!'".format(Fish.__name__, self.name))

    def eat(self, food):
        print("{} {} likes eating {}".format(Fish.__name__, self.name, food))


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        print("{} {} makes noise: 'Gaw-gaw!'".format(Dog.__name__, self.name))

    def eat(self, food):
        print("{} {} likes eating {}".format(Dog.__name__, self.name, food))


if __name__ == '__main__':
    animal = Animal("Catty")
    duck = Duck("Galina")
    puppy = Dog("Spunky")
    fish = Fish("Goldy")
    animal.speak()
    animal.eat('apple')
    duck.speak()
    duck.eat('corn')
    puppy.speak()
    puppy.eat('bones')
    fish.speak()
    fish.eat('worms')
