"""
The interface-segregation principle (ISP) states
that no client should be forced to depend on methods it does not use.
ISP splits interfaces that are very large into smaller and more specific
ones so that clients will only have to know about the methods that are
of interest to them. Such shrunken interfaces are also called role interfaces.
ISP is intended to keep a system decoupled and thus easier to refactor,
change, and redeploy. ISP is one of the five SOLID principles
of object-oriented design, similar to the High Cohesion Principle of GRASP.
"""

from abc import abstractmethod


class Light(object):
    
    @abstractmethod
    def main_ligt():
        pass
    
    @abstractmethod
    def back_light():
        pass
    
    @abstractmethod
    def inside_light():
        pass

class Temp(object):

    @abstractmethod
    def temp_up():
        pass
    
    @abstractmethod
    def temp_down():
        pass


class Light_ctrl(Light):
    def main_ligt():
        print("Main light TURN ON")
    
    def back_light():
        print("Back light TURN ON")
    
    def inside_light():
        print("Inside light TURN ON")

class Temp_ctrl(Temp):

    def temp_up():
        print("Temp is ...UP")
    
    @abstractmethod
    def temp_down():
        print("Temp is ...DOWN")
#TODO
if __name__ == '__main__':

    class Dashboard(Light_ctrl):
        ml = Light_ctrl
        ml.main_ligt()
        ml.inside_light()

    class Great_class(Light_ctrl, Temp_ctrl):
        gclc = Light_ctrl
        gctc = Temp_ctrl
        #gc = Light_ctrl, Temp_ctrl
        gclc.main_ligt()
        gctc.temp_up()
