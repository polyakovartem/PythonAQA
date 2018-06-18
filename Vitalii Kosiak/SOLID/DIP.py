"""
The principle states:
A. High-level modules should not depend on low-level modules.
Both should depend on abstractions.
B. Abstractions should not depend on details.
Details should depend on abstractions.
"""

from abc import abstractmethod



class Visitors(object):
    """Describe..."""
    @abstractmethod
    def def_group(self):
        pass


class admin(Visitors):
    """Describe..."""
    def __init__(self, admin_name):
        self.a_n = admin_name
    def acess_list(self):
        """Describe..."""
        if self.a_n == 'adminname':
            return ('add', 'edit', 'delete', 'pass', 'view')
        else:
            return ('')


class moderator(Visitors):
    """Describe..."""
    def __init__(self, mod_name):
        self.m_n = mod_name
    def acess_list(self):
        """Describe..."""
        if self.m_n == 'moderatorname':
            return ('add', 'edit', 'view')
        else:
            return ('')

        
        
class regular(Visitors):
    """Describe..."""
    pass

        
if __name__ == '__main__':
    
    print('Acess to: ' +str(admin('adminname').acess_list()))
    


    
