from abc import abstractmethod


class IDiscount(object):

    @abstractmethod
    def calculate_amount(self):
        pass


class Order(IDiscount):

    def __init__(self, discount):
        self.discount = discount

    def calculate_amount(self):
        return self.discount * 0.5


class VipOrder(IDiscount):

    def __init__(self, discount):
        self.discount = discount

    def calculate_amount(self):
        return self.discount * 0.7


def main():
    Order(5).calculate_amount()
    VipOrder(10).calculate_amount()


if __name__ == '__main__':
    main()
