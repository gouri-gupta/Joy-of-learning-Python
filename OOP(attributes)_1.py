'''
class Dog:
    def __init__(self,breed):
        self.breed=breed
m=Dog("Labrador")
print(m.breed)
'''





'''
class Cat:
    def __init__(self,my_breed):
        self.breed=my_breed
        print(my_breed)
c=Cat("Milli")
print(c.breed)
print(c.my_breed)#wil give an error because the attribute of the object is breed and not my_breed
'''




'''
class Donkey:
    def __init__(self,name,color,spots):
        self.name=name
        self.color=color
        self.spots=spots #will accept a boolean value ,foe example True/False
don=Donkey("Sammy","Brown",True)
print(don.name)
print(don.color)
print(don.spots)
'''