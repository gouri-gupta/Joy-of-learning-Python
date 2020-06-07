print("Write a program to print the pattern given below:")
print('''
* 

*+* 

*+*+* 

*+*+*+* 
''')
def func():
    for i in range(1,5):
        for j in range(1,i+1):
            if (j<i):
                print("*",end="+")
            else:
                print("*",end=" ")
        print("\n")

print("The above pattern can be printed by using the function func.The same pattern is obtained as shown below:")
func()
