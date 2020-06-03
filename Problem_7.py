print("Problem Statement 7:")
print('''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?''')

#If you enter a large number example,10001 as mentioned in the above problem you will have to wait for some seconds in order to get the output
def fun(k):
    l=[]
    n=2
    while (len(l)<k):
        for i in range(2,n):
            if (n%i==0):
                break
        else:
            l.append(n)
        n+=1
    print(l)
    print(max(l),"is the",k,"th prime number")
k=int(input("Which prime number do you want that is at which position:"))
#for example as mentioned in the above problem 6th prime mumber or 10001st prime number
fun(k)