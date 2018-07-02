import collections
import hashlib
import os.path

adress = 'E:/E_C_Work'

class WithoutName:
    
    def __init__(self, adress):
        self.adress = adress
        
    count = 0
    data = collections.defaultdict(list)  # u
    delete_list = []
    datal1 = collections.defaultdict(list)
    datal2 = collections.defaultdict(list)

    def read_fsize_fname(self, adress):
        for root, dirs, files in os.walk(adress):
            for filename in files:
                fullname = os.path.join(root, filename) #create fullname
                key = os.path.getsize(fullname) #get size of files
                self.data[key].append(fullname) #add in value full name of files
                self.count += 1
        '''
        for i in self.data:
            if len(self.data[i]) > 1:
                print(i, ' byte', self.data[i], str(len(self.data[i])) + ' Files has the same size.')
            else:
                print(i, ' byte', self.data[i], str(len(self.data[i])) + ' Files.')
        '''             
        print('\nCount of file is :', self.count)

                
    def delete_fsingle(self):
        for i in self.data:
            if len(self.data[i]) == 1:
                self.delete_list.append(i)
        
        for i in self.delete_list:
            self.data.pop(i)
        self.delete_list.clear()
        '''
        print(' ')
        for i in self.data:
            print(i, ' byte', self.data[i], str(len(self.data[i])) + ' Files has the same size.')
        '''


    def create_hashlist_level1(self):
        print(' ')
        try:
            for i in self.data:
                for k in self.data[i]:
                    with open (k, 'rb') as f:
                        temp = hash(f.read(1024))
                        self.datal1[temp].append(k)
        except:
            print (Exception)

        
    def create_hashlist_level2(self):
        print(' ')
        try:
            for i in self.datal1:
                if len(self.datal1[i]) != 1:
                    for k in self.datal1[i]:
                        with open (k, 'rb') as f:
                            temp = hash(f.read())
                            self.datal2[temp].append(k)
        except:
            print (Exception)

                      
    def duplicate(self):
        self.read_fsize_fname(self.adress)
        self.delete_fsingle()
        self.create_hashlist_level1()
        self.create_hashlist_level2()

        for i in self.datal2:
            if len(self.datal2[i]) != 1:
                print (self.datal2[i])


session = WithoutName(adress)
session.duplicate()
