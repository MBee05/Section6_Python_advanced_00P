class PlayerCharacter:
    
    membership = True
    def __init__(self, name, age):
            self.name = name 
            self.age = age
            
        
        
        
    def shout(self):
        print(f'my name is {self.name}')       
    
    
    # when use classmethod u dont need to instancitate
    @classmethod
    def adding_things(cls,num1,num2):
        return cls('Teddy',num1 + num2)
    #with cls I instancitate an object 'teddy'            output  <__main__.PlayerCharacter object at 0x0000025D4EECFC90>
        # cls is the playercharacter
        
        
#this method is same as classmethod except no access to 'cls'
# we use this method when we dont care about the attributs as name, age etc
    @staticmethod
    def adding_things2(num1,num2):
        return num1 + num2  
        
        
        
# player1 = PlayerCharacter('cindy', 44)
print(PlayerCharacter.adding_things(2,3))       

player3= PlayerCharacter.adding_things(2,3)
print(player3.age)

