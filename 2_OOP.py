# OOP
    # we are working in gaming company
    # naming convention class and have to be singular bcz its a blue print
    # when u building a class, this is called constructive method or init method
                        # name is the name of the player
class PlayerCharacter:
    def __init__(self, name, age): # self refer to the player character
        # these are attributes or proprieties
        self.name = name 
        self.age = age
        
        
    def run(self): #Function which doesn't return anything
        print('run')
    

# one piece of code with diff players which are saved in diff place in memory, we can use this code over and over to create  our own object
        
player1 = PlayerCharacter('cindy', 44)
# run is a method
print(player1.run())
# result    None why? bcz the above function which doesn't return anything


print(player1)
#output
# <__main__.PlayerCharacter object at 0x0000023B10F5F4D0>
print(player1.name)
print(player1.age)


player2 = PlayerCharacter('tom', 23)
print(player2.age)
# <__main__.PlayerCharacter object at 0x0000023B10F5F610> are stored in diff memory

player2.attack =50
print(player2.attack)

player3 = PlayerCharacter('carl',45)

# tips display blue print
help(player1)
help(list)



