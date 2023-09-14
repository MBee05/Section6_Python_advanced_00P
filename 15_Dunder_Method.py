# DUNDER METHOD

from typing import Any


class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.my_dict={
            'name':'Yoyo',
            'has_pets':False
        }
        
    def __str__(self):
        return f'{self.color}'        #bcz of that  
        
    def __len__(self):
         return 5
     
    def __del__(self) :
        print('deleted!')
        
    def __call__(self):
        return('yessss????')
        
    def __getitem__(self,i):
        return self.my_dict[i]
            
        
action_figure = Toy('red', 0)
print(action_figure.__str__()) #Dunder M
# 2 way of printing 
print(str(action_figure))           #red
                                    #red
print(len(action_figure))           #5                                
del action_figure                   #deleted
# print(action_figure())              #yes??
print(action_figure['name'])        #Yoyo