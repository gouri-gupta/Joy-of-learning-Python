#rishabhj@nvidia.com
#Create a generator that generates the squares of numbers up to some number N.

'''
def create_square(n):
    for i in range(n):
        yield i**2
n=int(input("Enter a number:"))
for x in create_square(n):
    print(x)
'''




#Create a generator that yields "n" random numbers between a low and high number (that are inputs).

'''
from random import*
def ran(low,high,n):
    for i in range(n):
        yield randint(low,high)
while True:
    try:
        n=int(input("Enter the number of random numbers you want:"))
        l=int(input("Enter the lower bound(number):"))
        h=int(input("Enter the upper bound(number):"))
    except:
        print("Please enter a number")
        continue
    else:
        print("The random numbers are:")
        for number in ran(l,h,n):
            print(number,end=" ")
        break
'''





'''Use the iter() function to convert the string below into an iterator:
s = 'hello'
'''

'''
s="hello"
a=iter(s)
for i in range(len(s)): #instead of writting next() function 5 times again and again
    print(next(a))
'''




'''Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.'''
#Don't know
'''If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, 
you would want to use a generator. (Multiple answers are acceptable here!)'''



#GOOD LOGICAL QUESTION
'''
my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)
print(gencomp)
print(type(gencomp))
print(list(gencomp))
for item in gencomp: #this for loop will not execute i.e it won't print any numbers once the above line of code i.e list is executed because generator function has been executed
    print(item)
#print(next(gencomp)) #will give an error STOP ITERATION because the generator function has been executed
'''