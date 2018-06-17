'''
This example ilustrates a violation of Dependency Inversion principle
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
    def __init__(self):
        self._engine = Engine()
        
    def getEngineRPM(self):
        return self._engine.getRPM();
