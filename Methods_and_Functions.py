'''Typically we use the return keyword to send back the result of the function,instead of just printing it out.
"Return" allows us to assign the output of the the function to a new variable'''

#Variable length arguments :In order to accept multiple arguments
#When we don't know how many arguments the user want ot pass
# defined by using "*" (asterik)
#takes arguments in the form of tuple
'''def fun(*args):
    """This function returns the sum of two or more than two numbers"""
    print(args)
    return sum(args)
z=fun(10,20)
print(z)
print(fun.__doc__)#this line return the documentation string present for a given function
#Remember documentation string must be the first line of the function definition
'''


#keyworded arguments
#In order to pass the arguments in the form of "key=value" pairs
'''def func(**kwargs):
    """This function illustrates an example of Keyworded arguments"""
    print(kwargs)
    if "fruit" in kwargs:
        print("My favourite fruit is {}".format(kwargs["fruit"]))
    else:
        print("I did not find my favourite fruit")
p=func(fruit="Pineapple",vegetable="Lady's Finger")
print(p)# the function doesn't return anything
print(func.__doc__)
'''



# an example of combination of keyworded and variable length arguments
'''def function(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs["food"]))
function(10,20,30,fruit="Pineapple",food="Choco Chips")
# Avoid mixing the keyworded and variable length/positional arguments otherwise Python will generate an error 
#Keyworded arguments should always follow the positional arguments that is they must be placed at the end as shown in the above example 
'''