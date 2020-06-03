#Decorators allow you to decorate a function
#Decorators allow you to tack on extra functionality to an already existing function
#They use the @ operator and rae then plced at the top of the original function
'''
def hello():
    return "Hello!"
print(hello())
print(hello) #will return what is "hello" and is present at which memory location
greet=hello
print(greet())
del hello
#hello()  makes sense that it will give  error because we have just now deleted hello function
print(greet())
print(greet)#it is nothing but simply a copy of the hello function
'''





'''def hello(name="Gouri"):
    print("The hello() function has been executed")

    def greet():
        return "\t The greet() function inside the hello function has been executed"

    def welcome():
        return "\t The welcome() function inside the hello function has been executed"

    print("I am going to return a function")
    if (name=="Gouri"):
        return greet
    else:
        return welcome
z=hello("Gouri") #will return the greet function that is z=greet
print(z)
print(z())
'''




'''def cool():
    def super_cool():
        return "I am super cool"
    return super_cool
p=cool()
print(p)
print(p())
'''



'''def hello():
    return "Hello World"
def new_function(some_other_function):
    print("Other code runs here!")
    print(some_other_function())
print(hello)
print(hello())
new_function(hello)
'''




#MAIN PART OF THE DECORATOR

#Complicated without the use of decorator
def new_decorator(original_func):

    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")

    return wrap_func

'''
def func_needs_decorator():
    print("I want to be decorated")

#func_needs_decorator()#the function won't get decorated
z=new_decorator(func_needs_decorator)#z=wrap_func
print(z)#will print out what is z
z()#will execute the wrap_func function which is returned from the new_decorator function
'''



#Easy way with the help of DECORATOR
@new_decorator #This line will pass the fun_need_decorator function as an argument for the new_decorator function and perform all the necessary operations on it and return the results
#If you want to remove this extra functionality of new_decorator function you can simply comment the above line as #@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
func_needs_decorator() #will give the same output as that for the above code
