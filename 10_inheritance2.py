
class User:
    def sign_in(self):
        print('logged in')
        
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


wizard1 = Wizard('merlin', 60)
# isinstance(instance,Class)
print(isinstance(wizard1,Wizard))
# output    True- bcz wizard or wizard1 is an instance of Wizard

# is it wizard1 is an instance of User bcz we have to the user class to  creare wizard1 
print(isinstance(wizard1,User))