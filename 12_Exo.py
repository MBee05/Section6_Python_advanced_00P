class Pets():
    animals = []
    def __init__(self, animals):
        self.animals= animals
        
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
            
class Cat():
    is_lazy =True
    
    def __init__(self, name,age):
        self.name=name
        self.age=age
    
    def walk(self):
        return f'{self.name} is just walking around'
    
class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
    
# 1 Add another Cat
class Wishu(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
# 2 Create a list of all the pets(creates 3 cat instances from the above)
my_cats=[Simon('Simon', 3), Sally('Sally', 2), Wishu('Wish', 1)]
print(my_cats)

# output    [<__main__.Simon object at 0x000001D9A61C8810>, <__main__.Sally object at 0x000001D9A61C8510>, <__main__.Wishu object at 0x000001D9A61C8350>]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)


# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
#Simon is just walking around
# Sally is just walking around
# Wish is just walking around 




