class SmartCar:
    @staticmethod
    def print_car():
        print("This transport can go on road")

class SmartPlain:
    @staticmethod
    def print_plain():
        print("This transport can fly in the air")

class SmartShip:
    @staticmethod
    def print_ship():
        print("This transport can go in the water")

class MegaSmartTransport(SmartCar, SmartPlain, SmartShip):
    @staticmethod
    def print_super():
        print("This is a supertransport")

SmartCar.print_car()
SmartPlain.print_plain()
SmartShip.print_ship()
MegaSmartTransport.print_super()
MegaSmartTransport.print_car()
MegaSmartTransport.print_plain()
MegaSmartTransport.print_ship()
