# MRO _ Method Resolution Order= is rule that python follows to determine when u run a method which one to run, when u have such a complicated inheritance structure

class A:
    num =10
    
class B(A):
    pass

class C(A):
    num = 1
    
class D(B,C):   #D inherit from B C 
    pass

print(D.num)     #so output  1

print(D.mro())    #[<class '__main__.D'>, <class '__main__.B'>,       <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]     =Order of checking




