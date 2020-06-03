en=input("Enter your employee name")
ei=input("Enter your employee id")
b=input("Enter the basic salary")
if (b.isdigit()):
    if (int(b)>=1):
        hra=(int(b))*0.1
        ta=int(b)*0.05
        total=int(b)+hra+ta
        tax=total*0.02
        nps=total-tax
        print(hra)
        print(ta)
        print(total)
        print(tax)
        print("Net payable salary is", nps)
    else:
        print("Enter a valid number")
else:
    print("Enter a valid integer number")

