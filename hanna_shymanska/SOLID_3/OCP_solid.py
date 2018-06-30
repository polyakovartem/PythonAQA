from abc import ABC, abstractmethod


class MusicalInstrument(ABC):
    @abstractmethod
    def play(self):
        pass

class Piano(MusicalInstrument):
    def __init__(self, press_key):
        self.press_key = press_key
    def play(self):
      print("Press a piano key")


class Saxophone(MusicalInstrument):
    def __init__(self, blow):
        self.blow = blow
    def play(self):
      print("Blow air into the instrument")


piano = Piano(42)
piano.play()
saxophone = Saxophone(23)
saxophone.play()