n=int(input("Enter the size of fibb series:"))
n1=0
n2=1
if (n<=0):
    print("Enter valid positive number")
elif (n==1):
    print("The fibb series is:")
    print(n1)
else:
    print("The fibb series is:")
    for i in range(1,n+1):
        print(n1,end=",")
        sum=n1+n2
        n1=n2
        n2=sum


