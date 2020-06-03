def strings(s,c):
    if (c.isdigit()):
        if (int(c)==1):
            print(len(s),"is the length of entered string")
        elif (int(c)==2):
            l=[]
            for i in range(len(s)-1,-1,-1):
                l.append(s[i])
            a=""
            for j in l:
                a+=j
            print("The reverse of entered string is:"+a)
        elif (int(c)==3):
            b=input("Enter the string to be compared:")
            if (len(s)==len(b)):
                if (s==b):
                    print("The string to be compared is equal to the entered string")
                else:
                    print("The entered strings are not equal")
            else:
                print("The entered strings are not equal")
        elif (int(c)==4):
            l = []
            for i in range(len(s) - 1, -1, -1):
                l.append(s[i])
            a = ""
            for j in l:
                a += j
            if (s==a):
                print("The entered string is a pallindrome")
            else:
                print("The entered string is not a pallindrome")
        elif (int(c)==5):
            m=input("Enter the substring to be checked:")
            if m in s:
                print("The entered substring is present at",s.find(m,0,len(s)),"index")
            else:
                print("ENTERED substring is not present in given string")

    else:
        print("Enter a valid number")
s=input("Enter the string:")
print("1.Length of string\n2.String reverse\n3.String comparison\n4.Check pallindrome\n5.Check substring")
c=input("Enter your choice:")
strings(s,c)


'''for i in range(0,len(s)):
            if (s[i]==m):
                print("Entered substring is present at",i,"index")'''