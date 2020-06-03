'''Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    print(i**2)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-c35f41ad7311> in <module>()
      1 for i in ['a','b','c']:
----> 2     print(i**2)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
'''

'''
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("The desired operation cannot be executed")
finally:
    print("End of the process")
'''







'''Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0

z = x/y

---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-6f985c4c80dd> in <module>()
      2 y = 0
      3 
----> 4 z = x/y

ZeroDivisionError: division by zero
'''

'''
def div():
    try:
        x=int(input("Enter first number:"))
        y=int(input("Enter second number:"))
        z=x/y
    except:
        print("The desired division operation cannot be performed on the entered numbers")
    else:
        print("The derired result of the division process is",z)
    finally:
        print("End of operation")
div()
'''







'''Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.'''

'''
def ask():
    while True:
        try:
            n=int(input("Enter a number:"))
        except:
            print("That's not a number")
        else:
            print("Thank you for providing a correct input")
            print("The square of",n,"is",n**2)
            break
        finally:
            print("I will always execute irrespective of whether there is an error or not")
ask()
'''
