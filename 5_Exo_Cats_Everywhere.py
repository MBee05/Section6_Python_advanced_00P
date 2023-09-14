# Given the below class:

class Cat:
    species = 'mammal'
    def __init__(self, name,age):
            self.name = name
            self.age = age
        
        

# 2 Create a funcion that finds the oldest cat
def find_oldest_cat(*args):
    return max(args)
       
            
            
            
            
# 1 Instantiate the Cat object with 3 cats
cat1=Cat('minou',6)
cat2=Cat('minou',4)
cat3=Cat('minou',2)


print(f'the oldest cat is {find_oldest_cat(cat1.age,cat2.age,cat3.age)} years old')

