'''
class Dog:
    #Class attributes
    species="Mammal"
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self,spots):
        print(f"Bow Bow!!!My name is {self.name}")
        print(f"The fact that I have spots on my {self.color} coloured body is {spots}")
d=Dog("Sammy","brown")
print(d.name)
print(d.color)
print(d.species)
print(d.bark)  #will return the address at which the result the bark function is stored
d.bark(True)
'''




'''
class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=self.pi*(self.radius**2)
    def circum(self):
        return 2*self.pi*self.radius
c=Circle(1)
print(c.pi)
print(f"The radius of the circle is {c.radius}")
print (f"The circumference of the circle is {c.circum()}")
print (f"The area of the circle is {c.area}")
'''
