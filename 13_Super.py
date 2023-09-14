class User(object):
    def __init__(self,email):
        self.email=email
        
    def sign_in(self):
        print('logged in')
        
     
# U have this way of doing it and there is another way which is called Super
class Wizard(User):
    def __init__(self, name, power,email):
        User.__init__(self,email)
        self.name=name
        self.power=power

    def attack(self):
        print(f'attacking with power of {self.power}')
    
    
wizard1 = Wizard('merlin', 60,'merlin@gmail.com')
print(wizard1.email)

# output    merlin@gmail.com


# Super is refering to the super Class which is above Wizard = User
class Wizard(User):
    def __init__(self, name, power,email):
        super().__init__(email)
        self.name=name
        self.power=power

    def attack(self):
        print(f'attacking with power of {self.power}')
    
    
wizard1 = Wizard('merlin', 60,'merlin@gmail.com')
print(wizard1.email)

# output    merlin@gmail.com
