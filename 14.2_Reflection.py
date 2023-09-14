# to examine, to modify at run time
# setattr(), __setattr__()

def __init__(self,name):
    self.name=name
    
def __getattr__(self,greet):
    
    def call__():
        greeting__msg = greet.replace("_"," ")
        
        print(f"{self.name}, {greeting__msg}")
        
    return call__



greeting = Greeting('Audrey')

greeting.nice_to_meet_you()
# output    Audrey, nice to meet you


greeting.good_morning()
# output    Audrey, good morning