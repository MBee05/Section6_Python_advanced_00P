# users can be 
# Wizards
# Archers
# ogres but all of them have to be signed in first
class User:
    def sign_in(self):
        print('logged in')
        
        # pass the parents class
   # these children classes are also called sub_classes or derived_classes
class Wizard(User):
    def __init__(self, name, power):
        self.name=name
        self.power=power

    def attack(self):
        print(f'attacking with power of {self.power}')
   
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name=name
        self.num_arrows=num_arrows

    def attack(self):
        print(f'attacking with arrows arrows left- {self.num_arrows}')


wizard1= Wizard('Merlin', 50)
archer1= Archer('Robbin', 100)
wizard1.attack()
# output    attacking with power of 50
archer1.attack()
# output    attacking with arrows arrows left- 100

