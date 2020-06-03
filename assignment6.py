def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
N=int(input("Enter any number:"))
z=reverse(N)
print(z)
l=[]
def rev(n):
    c=len(n)
    for i in range(c-1,-1,-1):
        l.append(n[i])
    for i in l:
        print(i,end="")
m=input("Enter any number:")
rev(m)
def rev(n):
    print("The reverse of the given number is:")
    rev=0
    while n>0:
        rem=n%10
        rev=rem
        n=n//10
        print(rev,end="")
m=int(input("Enter any number:"))
rev(m)



def rev(n):
    c=int(len(n))
    l=n[-1:-1-c]
    return l
n=input("Enter")
z=rev(n)
print(z)
