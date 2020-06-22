def func(n):
    print(n,"\n")
    s=input("Do you want to continue entering the name of the students\nType 'y' for yes and 'n' for no:").upper()
    if (s=="Y"):
        try:
            n=input("Enter the name of the student:")
            if (n.isalpha()):
                func(n)
            else:
                print("That's not a name.Please enter a name!")
                func(n="Please provide a valid input")
        except:
            print("That's not a name.")
    elif (s=="N"):
        print("The recursive function finally ended!")
        return
    else:
        func(n="Please provide a valid input")
n=input("Enter the name of the student:")
func(n)