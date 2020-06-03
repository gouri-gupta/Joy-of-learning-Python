#range function
'''range(0,10)
print(range(0,10))#this won't print the actual numbers i.e from 1 to 10
#In order to print the actual numbers ie from 1 to 10 you will have to print it in the form of list
print(list(range(0,10)))'''


'''word="abcde"
#enumerate() function
for item in enumerate(word):
    print(item)'''


#zip fuction
'''l1=[1,2,3]
l2=['a','b','c']
zip(l1,l2)
print(zip(l1,l2))#this won't return the result of the operation but it will return the address at which the result of the above operation is stored
for item in zip(l1,l2):
    print(item)
#we can do this operation of zip function with mutiple lists
l3=["one","two","three"]
for item in zip(l1,l2,l3):
    print(item)
print(list(zip(l1,l2,l3)))
for i,j,k in zip(l1,l2,l3):
    print(i)
    print(j)
    print(k)
    print("\n")
l4=[100,200,300,400]#it will exclude 400 if the number of elements in the list are uneven
print(list(zip(l1,l2,l3,l4)))'''


#Random Module in pyhton
'''from random import shuffle
#never use "list" as a variable name in python because it is a keyword in python which is required to convert any datatype into a list datatype
mylist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(shuffle(mylist))#shuffle(any_list) will return nothing as shown in  this line of code
print(mylist)
from random import randint
print(randint(0,100))#wil return any random number in between 0 to 100 and the output will be different everytime you execute the code
print(randint(0,100000))
'''



#list comprehension operators
'''mystring="hello"
mylist=[letter for letter in mystring]
print(mylist)
word="word"
l=[x for x in word]
print(l)
l1=[x for x in range(0,10)]
print(l1)
print([x**2 for x in range(0,10)])
print([x for x in range(0,11) if x%2==0])
print([x if x%2==0 else "ODD" for x in range(0,11) ])
combined_list=[x*y for x in [1,2,3] for y in [1,10,100,1000]]
print(combined_list)
list_1=["Hello"]
list_2=["Gouri","Yuvraj","Krishna","Vaishnavi"]
l3=[x+" "+y+"!" for x in list_1 for y in list_2]
for i in l3:
    print(i)'''
