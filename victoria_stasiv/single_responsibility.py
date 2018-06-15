from abc import ABCMeta, abstractmethod
class IPurchase(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def setSeller(self, seller):
        pass
    @abstractmethod
    def setBuyer(self, buyer):
        pass
    @abstractmethod
    def setBrand(self, brand):
        pass
class IBrand(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def getString(self):
        pass

class MyBrand(IBrand):
    def __init__(self, brand):
        self.brand = brand
    def getString(self):
        return "{}".format(self.brand)
class Purchase(IPurchase):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__seller = None
        self.__buyer = None
        self.__brand = None
    def setSeller(self, seller):
        if self.protocol == 'IM':
            self.__seller = ''.join(["I'm", seller])
        else:
            self.__seller = seller
    def setBuyer(self, buyer):
        if self.protocol == 'IM':
            self.__buyer = ''.join(["I'm", buyer])
        else:
            self.__buyer = buyer
    def setBrand(self, brand):
        self.__brand = brand.getString()

    def __repr__(self):
        template = "Seller: {seller}\nBuyer: {buyer}\nBrand:\n{brand}"
        return template.format(seller=self.__seller, buyer=self.__buyer, brand=self.__brand)

def main():
    purchase = Purchase('IM')
    purchase.setSeller(' Ann')
    purchase.setBuyer(' James')
    brand = MyBrand('Apple')
    purchase.setBrand(brand)
    print(purchase)
if __name__ == '__main__':
    main()




