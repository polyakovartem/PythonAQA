'''
To uncouple Vehicle's dependency from Engine we must make
the Vehicle class stop taking responsibility for
instantiating the Engine object, injecting it
as a parameter to the constructor.
'''
class Engine:
    def __init__(self):
        pass
      
    def accelerate(self):
        pass
 
    def getRPM(self):
        currentRPM = 0
        #...
        return currentRPM
 
class Vehicle:
    def __init__(self, engine):
        self._engine = engine
        
    def getEngineRPM(self):
        return self._engine.getRPM();
