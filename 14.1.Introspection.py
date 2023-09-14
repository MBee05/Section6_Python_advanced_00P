# type introspection
# to examine an object at runtime
# dir(), object.__dict__
# type(). isinstance(), issubclass()


class Pet:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        print(self.name)
        

class Clownfish(Pet):
    def swim(self):
        print(f'{self.name}, swim')
        

marvin = Clownfish('Marvin')
marvin.get_name=lambda:print('Hello')

# {'name': 'Marvin', 'get_name': <function <lambda> at 0x000001ADB4B70540>}



print(dir(marvin))
# output['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_name', 'name', 'swim']

# it will give you all the method & attributs that Wizard instance has 

print(marvin.__dict__)
# {'name': 'Marvin'}                 it gives the key value

print(type(marvin))
# <class '__main__.Clownfish'>      

print(isinstance(marvin, Clownfish))
# True

print(issubclass(Clownfish, Pet))
# True