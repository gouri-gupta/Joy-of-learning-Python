#Generator function allow us to write a function that can send back a value and then later resume to pick up where it left off
#Generator allow us to generate a sequence of values over time
'''The advantage of generator function is that instead of having to compute an entire series of values up front,the
generator computes one value waits until the next value is called for'''
#For example range(1,10) i.e if we want to print the numbers between 1 to 10 we would have to do list(range(1,10))
'''Thus range() function is an example of generator i.e instead of remembering all the numbers between 1 to 10 and instead of storing a giant list containing 
numbers between 1 to 10 in memory,it just remembers the start ,stop and step and generates the numbers as they come'''

'''def create_cube(n):
    result=[]
    for i in range(n):
        result.append(i**3)
    return result
print(create_cube(10))
for j in create_cube(5):
    print(j)
'''


#Concept of Generator
#IMPORTANT CONCEPT TO TAKE AWAY
'''def create_cube(n):
    for i in range(n):
        yield i**3    #more memory efficient way if suppose we had n=1 million
print(create_cube(5)) #will tell that you have a generator object here at the respective location in memory
print(list(create_cube(5))) #Since yield option is already mentioned in the function this option of printing list is avoided in order tobe memory efficient
for j in create_cube(5): #iterating through the generator
    print(j)
'''




#generating fibbonacci series
#more memory efficient way using yield function

'''
def fibb(n):
    #This function will generate n fibbonacci numbers
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
print(fibb.__doc__)
for x in fibb(5):
    print(x,end=",")
'''



#next() function
'''
def simple_gen():
    for x in range(3):
        yield x
for num in simple_gen():
    print(num)
g=simple_gen()
print(g);print(type(g))
print(next(g))
print(next(g)) #remembers the previous value and calculates the next value according to the formula ,it's not holding everything in memory
print(next(g))
#print(next(g))#it will give an error of stop iteraration because all the values have been yielded
'''




#iter() function
#iter function allows us to basically iterate through a normal object that you may not expect
'''
s="hello"
#iterarting through the string without using the iter() function
for letter in s:
    print(letter)
print("\n")
print("By using iter function:")
#we cannot use next() function for this
#print(next(s)) #will give an error i.e we cannot directly iterate over a string object by using next() function
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
#print(next(s_iter))  #will give an error "STOP ITERATION"
'''
