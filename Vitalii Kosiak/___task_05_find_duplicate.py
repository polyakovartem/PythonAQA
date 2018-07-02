import collections
from collections import Counter

import os
import os.path

import hashlib

adress = 'E:/test'
#name_size = collections.defaultdict(list)
hashdict = {}

def get_files(adress):
    
    data = collections.defaultdict(list)
    name_size = collections.defaultdict(list)
    num = 1
    
    for root, dirs, files in os.walk(adress):
        for filename in files:
            fullname = os.path.join(root, filename)
            key = (os.path.getsize(fullname), filename)
            data[key].append(fullname)
            
            name_size[fullname].append(os.path.getsize(fullname))

    for i in data:
        #print ('{} {} {} \n'.format(str(num), i, data[i]))
        num += 1

    num = 1
        
    for i in name_size:
        #print ('{} {} {} \n'.format(str(num), i, name_size[i]))
        num += 1

    #hashdict = {}
    
    for i in name_size:
        with open(i, 'r') as f:
            d = f.read()
        hashdict[i] = hash(d)

    hashlistn = []
    hashlistc = []

    for i in hashdict:
        hashlistn.append(i)
        hashlistc.append(hashdict[i])

    #print (hashlistn)
    #print (hashlistc)

    k = 0
    
    for i in range(k, len(hashlistc)):
        for x in range(k + 1, len(hashlistc)):
            if hashlistc[i] == hashlistc[x]:
                print (str(hashlistn[i]) + '  ==  ' + str(hashlistn[x]) )
        k = k + 1
