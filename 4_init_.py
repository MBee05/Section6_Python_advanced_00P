class PlayerCharacter:
    
    membership = True
        # can change as following
        # def __init__(self,  name='anonymous', age=0):
    def __init__(self, name, age):
        # only ppl over 18
        if (age > 18):  
            self.name = name 
            self.age = age
            
        
        
        
    def shout(self):
        print(f'my name is {self.name}')       
    

        
player1 = PlayerCharacter('cindy', 44)
player2 = PlayerCharacter('tom', 10)
player2.attack =50


# print(player2.shout())        output 'my name is tom'
# print(player2.shout())        output 'error' bcz tom is only 10