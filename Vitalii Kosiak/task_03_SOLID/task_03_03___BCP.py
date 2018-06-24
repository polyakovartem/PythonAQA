"""
LSP (Liskov substitution principle) 
"""

from abc import abstractmethod


class Printer (object):
    
    def start_print(self):
        pass

    def stop_print(self):
        pass


class Main_comp(Printer):

    def start_print(self):
        print ('Printing...')

    def stop_print(self):
        print('Stop')

class Another_device(Printer):
    def start_print(self):
        print ('Printing...')

    def stop_print(self):
        print('Stop')

class Copy1(Main_comp):
    def make_copy(self):
        print('START PRINT...')
        Main_comp.start_print(self)
        Main_comp.stop_print(self)
        print('FINISH')
        
if __name__ == '__main__':
    c1 = Copy1()
    c1.make_copy()
