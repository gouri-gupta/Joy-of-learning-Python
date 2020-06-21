print("Problem:Binary to Decimal and Back Converter")
print("Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent")
def isbin(n):
    for i in n:
        if (i!="1" and i!="0"):
            return False
    else:
        return True





def convert_to_binary(n):
    a=""
    while (n!=0):
        r=n%2
        n=n//2
        a+=str(r)
        continue
    return a[::-1]

def convert_to_decimal(n):
    k=n[::-1];l=list(k)
    s=0
    for i in range(len(l)):
        s+=(int(l[i])*(2**i))
    return s

def bina():
    try:
        n=int(input("Enter the number:"))
        print("The binary equivalent of",n,"is",convert_to_binary(n))
    except:
        print("Please provide a number!")
        bina()

def deci():
        try:
            n = input("Enter a binary number:")
            z=isbin(n)
            if (z==False):
                deci()
            else:
                print("The decimal equivalent of", n, "is", convert_to_decimal(n))
                return
        except:
            print("Please provide a binary number!")
            deci()


while True:
    try:
        p=input(print("For decimal to binary converter enter 1\nFor binary to decimal converter enter 0\nEnter your choice as per the desired operation:"))
        if (p=="1"):
            bina()
            break
        if (p=="0"):
            deci()
            break
        if (p!="0" and p!="1"):
            print("Please provide a valid input!")
            continue
    except:
        print("Please provide a valid input!")
        continue
