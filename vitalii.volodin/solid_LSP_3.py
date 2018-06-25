class Car:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print('Wroom...')


class FuelCar(Car):
    def fill_fuel_tank(self, liters):
        print('You bought {} liters of fuel for {}'.format(liters, self.model))


class ElectricCar(Car):
    def charge_battery(self, kw):
        print('You bought {} kW for {}'.format(kw, self.model))


class Mercedes(FuelCar):
    def start_engine(self):
        print('Mercedes wroom.')


class Fiat(FuelCar):
    def start_engine(self):
        print('Fiat wroom.')


class Nissan(ElectricCar):
    def start_engine(self):
        print("It's electric car. There is no wroom.")


class Tesla(ElectricCar):
    def start_engine(self):
        print("It's Tesla. There is no wroom.")


def main():
    fuel_cars = (Mercedes('AMG E63s'), Fiat('500'))
    electric_cars = (Nissan('Leaf'), Tesla('Model S'))

    for car in fuel_cars:
        car.start_engine()
        car.fill_fuel_tank(20)

    print("-" * 20)

    for car in electric_cars:
        car.start_engine()
        car.charge_battery(35)


if __name__ == '__main__':
    main()

