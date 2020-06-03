print("Problem Statement 10:")
print('''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.''')

#This program will take more time to execute if very large number is entered as mentioned in the above case
def fun(k):
    s=0
    for n in range(2,k):
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            s+=n
    return s
k=int(input("Enter the number below which you ant the sum of all the primes:"))
print(fun(k))