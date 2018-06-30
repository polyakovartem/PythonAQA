import collections
from collections import Counter
import os
import os.path

adress = 'E:/test'
#name_size = collections.defaultdict(list)

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
        print ('{} {} {} \n'.format(str(num), i, data[i]))
        num += 1

    num = 1
        
    for i in name_size:
        print ('{} {} {} \n'.format(str(num), i, name_size[i]))
        num += 1


        
        

