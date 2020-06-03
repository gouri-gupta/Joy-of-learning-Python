'''import math
def square(n):
    result=n*n
    print("The square of the entered number is:",result)
n=int(input("Enter any number:"))
square(n)
def evenodd(a):
    if (a%2==0):
        print("Entered number is even")
    else:
        print("Entered number is odd")
a=int(input("Enter any number:"))
evenodd(a)
def squarerootcube(b):
    sq=math.sqrt(b)
    c=b*b*b
    print("The square root of entered number is:",sq)
    print("The cube of entered number is:",c)
b=int(input("Enter any number b:"))
squarerootcube(b)
def prime(d):
    for i in range(2,d):
        if (d%i==0):
            print("Entered number is not prime")
            break
    else:
        print("Entered number is prime")
d=int(input("Enter any number:"))
prime(d)
def factorial(n):
    f=1
    for i in range(n,0,-1):
        if n==1:
            break
        else:
            f=f*i
    print("factorial of given number is:",f)
n=int(input("Enter any number:"))
factorial(n)'''
n=int(input("Enter any number:"))
l=[]
for i in range(2,n):
    if n%i==0:
        break
    else:
        l.append(i)
print(l)



