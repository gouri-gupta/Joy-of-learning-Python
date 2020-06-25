import json
from difflib import get_close_matches
#Note:load() method in order to load a entire json file and write the name of the file correctly in the open method otherwise it will givw a file not found error
#loads() method to convert a json object into a PYTHON object
data=json.load(open("original.json"))
#to check whether the json file is completely loaded or not into the program
#if you try to check the entire file this will lead to a clash because the file contains a very large amount of data
#therefore search only for a particular word,if you get its meaning means the entire json file is loaded

def check_for_wrong_word(n):
    k=1
    l1=get_close_matches(n,data)
    if (len(l1)!=0):
        print('You spelled it wrong.These might be the probable meanings of the word you are looking for.')
        for i in l1:
            lst = data[i]
            for j in range(0, len(lst)):
                print(str(k) + "." + lst[j])
                k+=1
        print()

        want_continue()
    else:
        print("Sorry!The meaning of the entered word doesn't exists in the dictionary")



def want_continue():
    try:
        y=input("Do you want to continue searching words in the dictionary?\nEnter 'y' for yes\nEnter 'n' for no:").upper()
        if (y=="Y"):
            func()
        elif (y=="N"):
            print("Hope you got the meaning of the desired words from the dictionary.\nThank-You")
        else:
            print("Please provide a valid input!")
            want_continue()
    except:
        print("Please provide a valid input!")
        want_continue()


def func():
    try:
        n=input("Enter the word:").lower()
        if (n.isalpha()):
            if (n in data):
                l=data[n]
                print("\nThe meaning of the word '"+n+"' is:")
                for i in range(0,len(l)):
                    print(str(i+1)+"."+l[i])
                print()
                want_continue()
            elif (n.upper() in data):
                l=data[n.upper()]
                print("\nThe meaning of the word '"+n+"' is:")
                for i in range(0,len(l)):
                    print(str(i+1)+"."+l[i])
                print()
                want_continue()
            elif (n.capitalize() in data):
                l=data[n.capitalize()]
                print("\nThe meaning of the word '"+n+"' is:")
                for i in range(0,len(l)):
                    print(str(i+1)+"."+l[i])
                print()
                want_continue()
            elif (n.title() in data):
                l=data[n.title()]
                print("\nThe meaning of the word '"+n+"' is:")
                for i in range(0,len(l)):
                    print(str(i+1)+"."+l[i])
                print()
                want_continue()
            else:
                check_for_wrong_word(n)
        elif (n.isnumeric()):
            print("That's a number and not a word.Please provide a word!")
            func()
        else:
           print("That's not a word!Please enter a word!")
           func()
    except:
        print("That's not a word.Please provide a word!")
        func()
func()