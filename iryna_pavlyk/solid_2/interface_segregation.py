"""
This module describes a homework related to SOLID.
Interface Segregation principle
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

from abc import abstractmethod


class Call:
    @abstractmethod
    def make_call(self):
        return "I can make a call"


class SaveNewNumber:
    @abstractmethod
    def save_number(self):
        return "I can save a new mobile number"


class TakePhoto:
    @abstractmethod
    def take_picture(self):
        return "I can take a picture"


class PlayGame:
    @abstractmethod
    def play_game(self):
        return "I can play a game"


class ConnectToInternet:
    @abstractmethod
    def connect_to_internet(self):
        return "I can connect to the Internet"


class SimpleMobilePhone(Call, SaveNewNumber, PlayGame):

    def __init__(self, made, model):
        self.made = made
        self.model = model


class SmartPhone(SimpleMobilePhone, TakePhoto, ConnectToInternet):

    def __init__(self, made, model):
        self.made = made
        self.model = model


if __name__ == '__main__':
    ericsson = SmartPhone("Sony-Ericsson", "I307")
    print(ericsson.save_number())
    print(ericsson.connect_to_internet())
    print(ericsson.make_call())
    print(ericsson.play_game())
    print(ericsson.take_picture())
    nokia = SimpleMobilePhone("Nokia", "3310")
    print(nokia.make_call())
    print(nokia.save_number())
    print(nokia.play_game())
