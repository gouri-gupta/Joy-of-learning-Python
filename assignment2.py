l=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(1,n+1):
    c=int(input("Enter the {} element of list".format(i)))
    l.append(c)
print("The list entered by the user is",l)
print("Maximum element of list is",max(l))
print("Minimum element of the list",min(l))
print("Sum of all the elments in the list is",sum(l))