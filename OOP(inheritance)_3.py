'''
class Animal:
    def __init__(self):
        print ("Animal Created")
    def who_am_i(self):
        print("I am an Animal")
    def eat(self):
        print ("I am eating")
a=Animal()


class Dog(Animal):
    def __init__(self):
        print("Dog Created")
        super(Dog, self).__init__()
    def who_am_i(self):
        print("I am a Dog")
        super(Dog, self).who_am_i()
d=Dog()
d.who_am_i()
d.eat()
'''





# another good example of INHERITANCE
'''
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):         # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement this abstract method")
a=Animal("Sam")
#a.speak()                               #you will get an error

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Bow Bow!!!")
d=Dog("Sam")
d.speak()

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!!!")
c=Cat("Milli")
c.speak()
'''





#POLYMORPHISM
'''
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())



for pet in [niko,felix]:
    print(pet.speak())



def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
'''