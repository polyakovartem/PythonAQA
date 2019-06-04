from abc import ABC, abstractclassmethod


@abstractclassmethod
class Engine(ABC):
        print(".... drive")


class DieselEngine(Engine):
    pass


class PetrolEngine(Engine):
    pass


class ElectroEngine(Engine):
    pass
