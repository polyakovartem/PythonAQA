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

    def listen_music(self):
        Driver().engage_ignition()
        Driver().inject_cd()
        Driver().turn_on_music()


class SecondDriver(ActivateCooler):

    def air_cooling(self):
        SecondDriver().engage_ignition()
        SecondDriver().swith_on_cooler()


def main():
    Driver().listen_music()
    SecondDriver().air_cooling()


if __name__ == '__main__':
    main()
