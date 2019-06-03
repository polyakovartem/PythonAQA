class IItem:
    def add_item(self):
        raise NotImplemented


class Gi(IItem):
    def __init__(self, brand, gi_size):
        self.brand = brand
        self.gi_size = gi_size

    def add_item(self):
        print('{}/[{}] gi was added.'.format(self.brand,
                                             self.gi_size))


class Pants(IItem):
    def __init__(self, brand, pants_size):
        self.brand = brand
        self.pants_size = pants_size

    def add_item(self):
        print('{}/[{}] pants was added.'.format(self.brand,
                                                self.pants_size))


class Belt(IItem):
    def __init__(self, color):
        self.color = color

    def add_item(self):
        print('{} belt was added'.format(self.color))


class RashGuard(IItem):
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def add_item(self):
        print('{}/[{}] rash guard was added'.format(self.brand,
                                                    self.size))


class BJJEquipment:
    def __init__(self, item):
        self.item = item

    def add_item(self):
        self.item.add_item()


def main():
    gi = Gi('Hayabusa', 'A3')
    pants = Pants('Hayabusa', 'A3')
    belt = Belt('blue')
    rashguard = RashGuard('Reebok', 'M')

    BJJEquipment(gi).add_item()
    BJJEquipment(pants).add_item()
    BJJEquipment(belt).add_item()
    BJJEquipment(rashguard).add_item()


if __name__ == '__main__':
    main()