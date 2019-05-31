from abc import ABC

class Engine(ABC): 
    def engine_type(self):
        print("No type defined")
 
class ElectroEngine(Engine):
    def engine_type(self):
        print("I am an Electro Engine")

class GasolineEngine(Engine):
    def engine_type(self):
        print("I am Gasoline Engine")

class Car:
    def __init__(self, engine_obj):
        self.engine = engine_obj

unknown_engine_car = Car(Engine())
unknown_engine_car.engine.engine_type()

electro_car = Car(ElectroEngine())
electro_car.engine.engine_type()

gasoline_car = Car(GasolineEngine())
gasoline_car.engine.engine_type()
