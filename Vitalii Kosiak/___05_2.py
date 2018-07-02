import collections
#import os
import os.path

catadress = 'E:/test'

class WithoutName:
    
    data = collections.defaultdict(list) #u
    name_size = collections.defaultdict(list) #u
    hashdict = {}
    hlinam = []
    hlicon = []
    k = 0
    
    def get_fullname_size(self, catalog):
        for root, dirs, files in os.walk(catalog):
            for filename in files:
                fullname = os.path.join(root, filename)
                key = (os.path.getsize(fullname), filename)
                self.data[key].append(fullname)
                self.name_size[fullname].append(os.path.getsize(fullname))
                
    def create_hash(self):
        for i in self.name_size:
            with open(i, 'r') as f: 
                d = f.read()
            self.hashdict[i] = hash(d)

    def compare(self):
        for i in self.hashdict:
            self.hlinam.append(i)
            self.hlicon.append(self.hashdict[i])
            
        for i in range(self.k, len(self.hlicon)):
            for x in range(self.k + 1, len(self.hlicon)):
                if self.hlicon[i] == self.hlicon[x]:
                    print (str(self.hlinam[i]) + ' == ' + str(self.hlinam[x]) )
            self.k += 1
            
if __name__ == '__main__':

    main = WithoutName()
    main.get_fullname_size(catadress)
    main.create_hash()
    main.compare()

    
