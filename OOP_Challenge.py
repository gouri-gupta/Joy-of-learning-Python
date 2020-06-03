'''For this challenge, create a bank account class that has two attributes:
owner
balance
and two methods:
deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.
'''

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print("Account Created")
        print(f"Hello!Mr/Mrs {self.owner}...Welcome to our bank.You currently have {self.balance} rupees in your bank account.")
    def deposit(self,deposit):
        self.balance+=deposit
        print(f"The total balnce available in your account is {self.balance} rupees")
    def withdraw(self,withdraw):
        if (withdraw>self.balance):
            print("Sorry!Money cannot be withdrawn from the bank because of insufficient balance...")
        else:
            self.balance=self.balance-withdraw
            print(f"{withdraw} rupees have been withdrawn from the bank.\nThe total balance available in your bank account is {self.balance} rupees")
o=input("Enter the name of the owner of the bank account:")
bal=int(input("Enter the balance available in your bank account:"))
b=BankAccount(o,bal)
def depo():
    n = input("Do you want to deposit money in your bank account?\nY for Yes\nN for No:")
    if (n=="Y" or n=="y"):
        k=int(input("Enter the amount you want to deposit in your bank account:"))
        b.deposit(k)
    elif (n=="N" or n=="n"):
        print("Thank you for visiting our bank...")
    else:
        print("Please enter a valid input!")
        depo()
depo()
def withd():
    n = input("Do you want to withdraw money in your bank account?\nY for Yes\nN for No:")
    if (n=="Y" or n=="y"):
        k=int(input("Enter the amount you want to withdraw from your bank account:"))
        b.withdraw(k)
    elif (n=="N" or n=="n"):
        print("Thank you for visiting our bank...")
    else:
        print("Please enter a valid input!")
        withd()
withd()