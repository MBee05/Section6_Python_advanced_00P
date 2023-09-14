class PlayerCharacter:
    def __init__(self, name, age):
            self.name = name 
            self.age = age
            
        
        
        
    def run(self):
        print('run')       
    
    
    def speak(self):
        print(f'my name is {self.name},and I am {self.age} yearsold')



player1 = PlayerCharacter('andrei', 100)  
player1.speak()  
        