"""
This module describes a homework related to homework with SOLID OCP.
"""
import random
import datetime as dt
from math import *
from abc import abstractmethod

class Calc:
    """Describe...."""
    def __init__(self, num, proc):
        self.proc = proc
    def take_1proc(proc):
        """Describe...."""
        return(str(proc/100))

class Exch(Calc):
    """Describe...."""
    pass

class Usd(Exch):
    """Describe...."""
    def __init__(self, val):
        self.value = val
        
    def usd_to_uah(value):
        print (str(value * 26))
    
    def uah_to_usd(value):
        return value * 0.038

class Eur(Exch):
    """Describe...."""
    def __init__(self, val):
        self.value = val
        
    def eur_to_uah(value):
        print (str(value * 30))
    
    def uah_to_eur(value):
        return value * 0.033

class Zlt(Exch):
    """Describe...."""
    def __init__(self, val):
        self.value = val
        
    def zlt_to_uah(value):
        print (str(value * 6))
    
    def uah_to_zlt(value):
        return value * 0.16
    
