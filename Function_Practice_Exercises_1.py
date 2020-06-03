#WARMUP SECTION:

'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
 but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''

'''def lesser_of_two_evens(a,b):
    if (a%2==0 and b%2==0):
        print(min(a,b))
    else:
        print(max(a,b))
p=int(input("Enter the first number:"))
q=int(input("Enter the second number:"))
lesser_of_two_evens(p,q)
'''






'''ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama')--> True
animal_crackers('Crazy Kangaroo') --> False'''

'''def animal_crackers(s):
    s=s.lower()
    l=[]
    for i in s.split():
        l.append(i)
    if (l[0][0]==l[1][0]):
        return True
    else:
        return False
n=input("Enter the two word string:")
print(animal_crackers(n))
'''


'''
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
text=input("Enter the string:")
print(animal_crackers(text))
'''


'''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''

'''def makes_twenty(a,b):
    if (a==20 or b==20):
        return True
    elif (a+b==20):
        return True
    else:
        return False
p=int(input("Enter the first number:"))
q=int(input("Enter teh second number:"))
print(makes_twenty(p,q))
'''

'''
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
'''


# Level 1 Problems
'''OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald'''

'''def old_macdonald(s):
    a=s.capitalize()
    p=a[:3]+s[3].upper()+a[4:]
    return p
s=input("Enter any name:")
z=old_macdonald(s)
print(z)
'''



'''
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
'''




'''MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We' 
'''

'''def master_yoda(s):
    l=[];l1=[]
    for i in s.split():
        l.append(i)
    l1=l[::-1]
    a=" ".join(l1)
    return a
s=input("Enter any string:")
print(master_yoda(s))
'''


'''
def master_yoda(text):
    return ' '.join(text.split()[::-1])
'''






'''ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True'''

'''def almost_there(n):
    if (n>=90 and  n<=110):
        return True
    elif (n>=190 and n<=210):
        return True
    else:
        return False
n=int(input(("Enter any number:")))
print(almost_there(n))
'''


'''
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
'''