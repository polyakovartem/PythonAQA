from abc import abstractmethod


class Venicle(object):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass


class Car(Venicle):

    def start_engine(self):
        Car.engage_ignition(self)
        print("Ignition successfully")

    def accelerate(self):
        print("vrummm vrummm")

    def engage_ignition(self):
        print("Ignition procedure")


class DieselCar(Venicle):

    def start_engine(self):
        DieselCar.engage_ignition(self)
        print("Ignition successfully")

    def accelerate(self):
        print("phhh phhhh")

    def engage_ignition(self):
        print("Ignition procedure")


class ElectricCar(Venicle):

    def accelerate(self):
        ElectricCar.connect_individual_engines(self)
        ElectricCar.increace_voltage(self)
        print("uuuuuuuuuuuuu")

    def increace_voltage(self):
        print("Voltage successfully increased")

    def connect_individual_engines(self):
        print("Individual engines is connected")


class FirstDriver(ElectricCar):

    def go(self):
        ElectricCar.start_engine(self)
        ElectricCar.accelerate(self)
        return print("Here we go!")


class SecondDriver(Car):
    def go(self):
        Car.start_engine(self)
        Car.accelerate(self)
        return print("Here we go too")


def main():
    FirstDriver().go()
    SecondDriver().go()


if __name__ == '__main__':
    main()
