class Vehicle:
    def __init__(self, max_speed=0, height=0, width=0, length=0):
        self.max_speed = max_speed
        self.height = height
        self.width = width
        self.length = length

    def move_vehicle(self):
        print('Vehicle moves')


class Car(Vehicle):

    def move_vehicle(self):
        self.run_engine()
        print('Vehicle moves')

    def run_engine(self):
        print("Car's engine is on")


class Motorcycle(Vehicle):

    def move_vehicle(self):
        self.run_engine()
        print('Vehicle moves')

    def run_engine(self):
        print("Motorcycle's engine is on")


class Bicycle(Vehicle):

    def move_vehicle(self):
        self.pedal()
        print('Vehicle moves')

    def pedal(self):
        print("Pedalling is in progress")


def main():

    vehicles = [Car(), Motorcycle(), Bicycle()]
    for vehicle in vehicles:
        vehicle.move_vehicle()


if __name__ == '__main__':

    main()
