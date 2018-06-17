'''
Correct use of Interface Segregation Principales.
'''

class Pet:
    def groom():
        pass
    
class Animal:
    def feed():
        pass

    
class Dog(Animal, Pet):
    def feed():
        pass
    def groom():
        pass #OK
    
    
class Snake(Animal):
    def feed():
        pass  #No need to groom!
