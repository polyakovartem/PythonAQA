'''
Correct use of Interface Segregation Principales.
'''

class Pet:
    def groom(self):
        return 'Groom the Pet'
    
class Animal:
    def feed(self):
        return 'Feed an Animal'

    
class Dog(Animal, Pet):
    def feed(self):
        return 'Feed an Dog'
    def groom(self):
        return 'Groom the Dog'
    
    
class Snake(Animal):
    def feed(self):
        return 'Feed the Snake'  #No need to groom!


Max = Dog()
print(Max.groom())

python = Snake()
print(python.feed())
print(python.groom())
