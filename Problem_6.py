print("Problem Statement 6:")
print('''The sum of the squares of the first ten natural numbers is,
12+22+...+102=385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.''')

def fun(n):
    sum=0
    sqr=0
    for i in range(0,n+1):
        sum+=i
        sqr+=i**2
    sum=sum**2
    print(sum)
    print(sqr)
    return sum-sqr
n=int(input("Enter the number of natural numbers desired for the above mentioned problem:"))
z=fun(n)
print("The difference between the sum of the squares of the first",n,"natural numbers and the square of the sum is",z)
