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


if __name__ == '__main__':
    o = Order(5).calculate_amount()
    vo = VipOrder(10).calculate_amount()
