#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' 
In this case, "Prisioner is a Person" relation can not directly applied to Person and 
Prisoner. The cause is that these two classes "behave" differently.
'''

class FreeMan:

    def __init__(self, position):
        self.position = position

    def walk_North(self, dist):
        self.position[1] += dist

    def walk_East(self, dist):
        self.position[0] += dist
        

'''
"Prisioner is a Person" relationship no longer holds since a `Prisoner` is not a FreeMan.
'''
class Prisoner:
    
    prison_location = (3, 3)

    def __init__(self):
        self.position = type(self).prison_location


def main():

    prisoner = Prisoner()
    print ("The prisoner trying to walk to north by 10 and east by -3.")
    
    try:
        prisoner.walk_North(10)
        prisoner.walk_East(-3)
    except:
        pass
    
    print("The location of the prison: {}".format(prisoner.prison_location))
    print("The current position of the prisoner: {}".format(prisoner.position))

if __name__ == "__main__":
    main()

