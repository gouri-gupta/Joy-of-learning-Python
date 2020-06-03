
def gcd(a,b):
    for i in range(c,1,-1):
        if a%i==0:
            if b%i==0:
                print("Greatest common divisor:",i)
                return i
                break
    else:
        print("Greatest common divisor is 1 and the entered numbers are coprime")
        return 1
def scd(a,b):
    if z>1:
        for i in range(2,z):
            if (z%i==0):
                print("Smallest common divisor is",i)
                break
        else:
            print("Smallest common divisor is 1")
    else:
        print("Smallest common divisor is 1")
N=int(input("Enter 1st number:"))
M=int(input("Enter 2nd number:"))
c=min(N,M)
z=gcd(M,N)
scd(M,N)
'''list=[1]
def gcd1(n1,n2):
    if (n1==1 or n2==1):
        print("Gcd is 1")
    else:
        for i in range(2,n1+1):
            if n1%i==0:
                for j in range(2,n2+1):
                    if n2%j==0:
                        if i==j:
                            list.append(i)
        print("GCD of given two numbers is",max(list))'''
#gcd1(M,N)









'''l=[1]
def rgt(a,b):
    for i in range(2,c+1):
        if a%i==0:
            if b%i==0:
                l.append(i)
    t=min(l) and min(l)!=1
    if (t==z):
        print("Smallest common divisor is 1")
    else:
        print("Smallest common divisor is",t)'''
