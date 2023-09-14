# We can custmize according our need
# polymorphism is the ability to redefine methods for these derived classes as wizrd & archer. AN object that are intentiated can behave in diff forms and ways  based on polymorphism
class User:
    def sign_in(self):
        print('logged in')
        
     
    def attack(self):
         print('do nothing')
        
        
class Wizard(User):
    def __init__(self, name, power):
        self.name=name
        self.power=power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')
     #output    'do nothing'  'attacking with power of 60'
   
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name=name
        self.num_arrows=num_arrows

    def attack(self):
        print(f'attacking with arrows arrows left- {self.num_arrows}')


wizard1 = Wizard('merlin', 60)
archer1 = Archer('robbin', 30)


# def player_attack(char):
#     char.attack()

# player_attack(wizard1)
# player_attack(archer1)

#output attacking with power of 60
# attacking with arrows arrows left- 30



# with for loop

# for char in [wizard1, archer1]:
#     char.attack()
    
# output    attacking with power of 60
# attacking with arrows arrows left- 30
