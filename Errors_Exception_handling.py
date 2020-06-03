'''The three most important keywords in the context of Errors and Exception Handling are:'''
#try:This is the block of code tobe attempted (may lead to an error)
#except:Block of code will execute in case there is an error in try block
#finally:A final block of code to be executed,regardless of an error


#Here the else block will be executed beause there is no error in the try block
'''
try:
    result=10+10
except:
    print("Hey!It looks like you aren't adding correctly.")
else:
    print("Add went well")
    print ("The required result is :",result)
'''

#Here there will be an error because you acnnot add a string to an integer,thus here the except block will be executed
'''
try:
    result=10+'10'
except:
    print("Hey!It looks like you aren't adding correctly.")
else:
    print("Add went well")
    print ("The required result is :",result)
'''

#Here there is no exception
'''
try:
    with open("filetest.txt","w") as f:
        f.write("Write a test line")
except:
    print("All other Exceptions")
finally:
    print("I always run")
'''



#Hre there will be an exception(error),because you hae opened the file in the "r" i.e read mode and you attempt to write in that file
'''
try:
    with open("filetest.txt","r") as f:
        f.write("Write a test line")
except:
    print("All other Exceptions")
finally:
    print("I always run")
'''


'''
def ask():
    try:
        n=int(input("Enter a number:"))
    except:
        print("Oops!That's not a number")
    finally:
        print("The desired operation is executed")
ask()
'''




#This function will continue to ask the user for the input until the user has provided correct input i.e a number
'''
def ask():
    while True:
        try:
            n = int(input("Enter a number:"))
        except:
            print("Oops!That's not a number.Please provide a number.")
        else:
            print("Thank You!You have provided a correct number")
            break
ask()
'''