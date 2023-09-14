# private?non true private variable so we do underscore in the attributes means it shouldn't be modified
class PlayerCharacter:
    def __init__(self, name, age):
        # _init_ its called 'Dunder Method'
            self._name = name 
            self._age = age
            
        
    def run(self):
        print('run')       
    
    
    def speak(self):
        print(f'my name is {self._name},and I am {self._age} yearsold')



player1 = PlayerCharacter('andrei', 100)  


print(player1.speak())
# output  my name is andrei,and I am 100 yearsold
# None

