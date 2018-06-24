#Create analog of wget application which downloads file,
#counts words and provides word statistics

'''Home task number 3'''


import urllib.request as ur
from collections import Counter

class Downloader ():
    '''This class contains download funtions'''
    
    def df (self, url):
        '''Function download txt! file and return its.Take url-adress.'''
        self.url = url
        
        if self.url[(len(self.url)-3):] == 'txt':
            try:
                resp = ur.urlopen(url)
                data = resp.read()
                return data.decode('utf-8')
            except:
                print('Smth is wrong!')
        else:
            print('Unknown format!')
            
    def get_filename (self, url):
        '''Description'''
        self.url = url
        if self.url[(len(self.url)-3):] == 'txt':
            tn = ' '
            fname = ' '
            ite = len(self.url) - 5
            
            while tn != '/':
                tn = self.url[ite]
                fname += tn
                ite -= 1
                
            fname = fname[::-1].replace('/','')
            return 'Name of file is: ' + '"' + fname.strip(' ').title()+ '"' + '\n'

            
class Mcounter ():
    '''Description'''
    
    def cw (self, phrase):
        '''Description'''
        self.phrase = phrase
        return len(phrase.split())
        
    
    def words_stat(self, phrase):
        '''Description'''
        nws = []; rws = []
        self.phrase = phrase
        ws = phrase.split()
        
        for i in ws:
            nws.append('Word: ' +'"'+ i +'"'+ ' = ' + str(ws.count(i)))

        for i in range(0, len(nws)):
            if nws[i] not in rws: rws.append(nws[i])      
        return rws

    def e_print(self, liiist):
        '''Description'''
        self.liiist = liiist
        for i in liiist:
            if i != None: print(i)

    def col_count (self, phrase):
        '''Description'''
        self.phrase = phrase
        return Counter(phrase.split())
             
                       
adress = 'http://myres.zzz.com.ua/test.txt'

d = Downloader()
c = Mcounter()
data = d.df(adress)

print(' ')
print('Adress of test file is: ' + '"http://myres.zzz.com.ua/test.txt"')
print(' ')
print(d.get_filename(adress))
print(data)
print(' ')
print('The number of words is: ' + str(c.cw(data)))
print(' ')
c.e_print(c.words_stat(data))
print(' ')
print(' ')
print(c.col_count(data))
