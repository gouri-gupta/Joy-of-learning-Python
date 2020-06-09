#A Normal tuple
t=(1,2,3)
print(t[0])
#The standard tuple uses numerical indexes to access its members as shown in the above example

#Here comes the concept of namedtuple
'''
For simple use cases, this is usually enough. On the other hand, remembering which index should be used for each value can lead to errors, especially 
if the tuple has a lot of fields and is constructed far from where it is used. A namedtuple assigns names, as well as the numerical index, to each member.
Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. 
The arguments are the name of the new class and a string containing the names of the elements.
The first argument is the name of the class and the second argument is a string containing the names of the elements i.e attributes of the class
In case the class has multiple attributes these attributes are represented by the string itself but are seperated by spaces as shown in the below example
You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields.
'''
from collections import*
'''
Dog=namedtuple("Dog","breed color name")
d1=Dog(breed="Lab",color="brown",name="Frankie")
print("Breed of dog",d1.breed,"\nColor of dog",d1.color,"\nName of dog",d1.name)
for i in range(3): #maintains the numerical index also
    print(d1[i])

Cat=namedtuple("Cat","name spots")
c=Cat("Kitty",False)
print("The name of the cat is",c.name,"and the fact that it has spots is",c.spots)
for i in range(len(c)):
    print(c[i])
'''

Student=namedtuple("Student","name class1 roll_no")
sam=Student(name="Samiksha",class1="Jr.Kg",roll_no=20)
print("The name of the student is",sam.name,"is studying in class",sam.class1,"with a roll number of",sam.roll_no)

#taking input from user
gouri=Student(name=input("Enter the name of the student:"),class1=input("Enter the class in which the student is studying:"),roll_no=int(input("Enter the roll number of the student:")))
print("The name of the student is",gouri.name,"is studying in class",gouri.class1,"with a roll number of",gouri.roll_no)