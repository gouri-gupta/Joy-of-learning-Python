from Die_Stimulator_design import*
from Die_Stimulator_designs_f import*
l=list(range(1,12))

def want_to_continue(n=1):
    ask=input("Do you want to continue playing with the stimulator?\nEnter 'Y' for yes\nEnter 'N' for no:").upper()
    cs = "func_type_" + str(n) + "()"
    try:
        if (ask=="Y"):
            exec(cs)
            want_to_continue(n)
        elif (ask=="N"):
            print("Hope You have enjoyed this game!\nWe look forward to see you again in this amusement.\nThank-You...")
        else:
            print("Please provide a valid input!")
            want_to_continue(n)
    except:
        print("Please provide a valid input!")
        want_to_continue(n=1)








def start_b():
    try:
        n=int(input("Select the type of Dice you want to play with.There are eleven types,specify the type by number:"))
        cs = "func_type_" + str(n) + "()"
        if (n in l):
            print("This is your desired dice.")
            exec(cs)
        else:
            print("Please provide a correct value!")
        want_to_continue(n)


    except:
        print("That's not a number.Please provide a number!")
        start_b()
start_b()