class Spam:
    __egg =7      #__privatemethod of class Spam
    def print_egg(self):
        print (self.__egg)

s=Spam()
s.print_egg()
print(s._Spam__egg)     '''could be accessed externally by _Spam__privatemethod '''
print(s.__egg)

'''
Basically, Python protects those members by internally changing the name to include the class name.
'''
