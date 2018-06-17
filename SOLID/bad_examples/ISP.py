'''
An example of the violation of Interface Segregation principle
'''

class Animal:
    
    def feed():
        pass
    def groom():
        pass
    

class Dog(Animal):
    
    def feed():
        pass
    def groom():
        pass #OK
    

class Snake(Animal):
    
    def feed():
        pass
    def groom():
        pass #Oops!!
