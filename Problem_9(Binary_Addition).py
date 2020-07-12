print("This program performs the Binary Addition of two numbers!")
def isbin(n):
    """This function checks whether the entered number is really a binary number or not"""
    for i in n:
        if (i!="1" and i!="0"):
            return False
    else:
        return True

#print(isbin.__doc__)

def convert_to_decimal(n):
    """This function converts the binary number into its equivalent decimal number"""
    k=n[::-1];l=list(k)
    s=0
    for i in range(len(l)):
        s+=(int(l[i])*(2**i))
    return s

#print(convert_to_decimal.__doc__)

def convert_to_binary(n):
    """This function converts the decimal number into its equivalent binary number"""
    a=""
    while (n!=0):
        r=n%2
        n=n//2
        a+=str(r)
        continue
    return a[::-1]

#print(convert_to_binary.__doc__)


while True:
    try:
        a=input("Enter the first binary number:")
        if isbin(a):
            while True:
                try:
                    b=input("Enter the second binary number:")
                    if isbin(b):
                        x = convert_to_decimal(a)
                        y = convert_to_decimal(b)
                        z = x + y
                        print(convert_to_binary(z), "is the result of binary addition of", a, "and", b)
                        #print(z,"=",x,"+","y") #in terms of decimal number
                        break
                    else:
                        print("Please provide a binary number!")
                        continue
                except:
                    print("Please provide a valid input!")
                    continue
            break
        else:
            print("Please provide a binary number!")
            continue
    except:
        print("Please provide a valid input!")
        continue



