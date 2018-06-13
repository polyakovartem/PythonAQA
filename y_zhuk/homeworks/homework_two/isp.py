from abc import abstractmethod


class PlayMusic(object):

    @abstractmethod
    def engage_ignition(self):
        pass

    @abstractmethod
    def inject_cd(self):
        pass

    @abstractmethod
    def turn_on_music(self):
        pass


class Cooler(object):

    @abstractmethod
    def engage_ignition(self):
        pass

    @abstractmethod
    def swith_on_cooler(self):
        pass


class ActivateMusic(PlayMusic):

    def engage_ignition(self):
        print("Ignition engaged")

    def inject_cd(self):
        print("CD is injected")

    def turn_on_music(self):
        print("la la la la la")


class ActivateCooler(Cooler):

    def engage_ignition(self):
        print("Engage ignition")

    def swith_on_cooler(self):
        print("Frost mode has activated")


class Driver(ActivateMusic):
    turn_on_music = ActivateMusic()
    turn_on_music.engage_ignition()
    turn_on_music.inject_cd()
    turn_on_music.turn_on_music()


class SecondDriver(ActivateCooler):
    turn_on_cool = ActivateCooler()
    turn_on_cool.engage_ignition()
    turn_on_cool.swith_on_cooler()
