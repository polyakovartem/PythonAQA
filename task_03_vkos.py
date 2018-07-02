"""
This module describes a homework related to homework with decorators.
"""

__author__ = 'Vitalii Kosiak'

title = 'solid'

for i in title:
    print((i).upper())
    
for i in range(0,3):
    print(' ')


#SRP

class CADD :
    
    a = 11
    b = 22
    
    def add99(n):
        return n + CADD.a
    
    def sub88(n):
        return n + CADD.sub88b



class CSUBB :
    
    a = 33
    b = 44

    def subb11(n):
        return n - CADD.a
    def subb11(n):
        return n - CADD.b


a = 12
print(CADD.add99(a))



#OCP
class CADD :
    
    _a = 11
    _b = 22
    
    def add99(n):
        return n + CADD.a
    
    def sub88(n):
        return n + CADD.sub88b



#LSP

print('Hi world!2')



