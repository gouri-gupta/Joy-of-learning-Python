#Write a function that computes the volume of a sphere given its radius.
'''
def volume_of_sphere(r):
    a=(4/3)*3.14*(r**3)
    return a
r=int(input("Enter the radius of the Sphere:"))
print("The volume of the sphre with radius",r,"is",volume_of_sphere(r))
'''






#Write a function that checks whether a number is in a given range (inclusive of high and low)
'''
def num_check(num,low,high):
    for i in range(low,high+1):
        if (num==i):
            return True
l=int(input("Enter the lower bound:"))
h=int(input("Enter the higher bound:"))
n=int(input("Enter the number you want to check whether it is in the given range or not:"))
z=num_check(n,l,h)
if (z==True):
    print(n,"is present in the desired range")
else:
    print(n,"is not present in the desired range")
'''

'''

def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

'''






#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
'''
def up_low(s):
    u=0
    l=0
    for i in s.split():
        for j in i:
            if (j.isalpha()):
                if (j.isupper()):
                    u+=1
                if (j.islower()):
                    l+=1
    return u,l
s=input("Enter the string:")
y,z=up_low(s)
print("The number of the uppercase and lowercase letters present in the given string are",y,"and",z)
'''

'''

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

'''






#Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''
def unique_list(l):
    print("Your list is:",l)
    a=set(l)
    return list(a)
l=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    a=int(input(f"Enter the {i+1} element of the list:"))
    l.append(a)
print(unique_list(l))
'''

'''

def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

'''






#Write a Python function to multiply all the numbers in a list.
'''
def mul(l):
    m=1
    for i in l:
        m*=i
    return m
l=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    a=int(input(f"Enter the {i+1} element of the list:"))
    l.append(a)
print("The multiplication of all the numbers present in the list",l,"is",mul(l))
'''






#Write a Python function that checks whether a passed in string is palindrome or not.
'''
def ispallindrome(s):
    return s==s[::-1]
print(pallindrome.__doc__)
s=input("Enter the string:")
print("The fact that the entered string",s,"is a pallindrome is",ispallindrome(s))
'''






#Write a Python function to check whether a string is pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#I have done it without using string module
'''
def ispangram(s):
    l=[]
    a=s.lower().split()
    for i in a:
        for j in i:
            if j.isalpha():
                l.append(j)
    k=set(l)
    if (len(k)==26):
        return True
    else:
        return False
s=input("Enter the string:")
print("The fact that the entered string is a pangram is",ispangram(s))
'''

#using string module
'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())

'''