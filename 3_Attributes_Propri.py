#OOP = allows us to write a code that is repeatable, well organised and also memory efficient
class PlayerCharacter:
    # class Object attributes, this cant be modify it, all the object that we instantiate will have access to
    membership = True
    def __init__(self, name, age):
        # checking if membership exist, only if membership is true then I will assign name & age
        # or can refer this code as following
        # if (PlayerCharacter.membership):
        if (self.membership):
            self.name = name 
            self.age = age
            
        
        
        
        # or we can do like
    # def shout(self):
        #print(f'my name is {self.name}')       
    def run(self):
        print('run')
        # return 'done'
    
    
    # def run(self,hello):
    #     print('run')
    #     # return 'done'
    
    

        
player1 = PlayerCharacter('cindy', 44)
# run is a method
# print(player1.run())
# result    now will return 'done'
# print(player1.shout())        output 'my name is cindy
# print(player1.run('hello'))   output 

# 


print(player1)
# result    = <__main__.PlayerCharacter object at 0x0000029E5E63F810>
print(player1.membership)
# result    = True
print(player1)
# print(player1.name)
# print(player1.age)


player2 = PlayerCharacter('tom', 23)