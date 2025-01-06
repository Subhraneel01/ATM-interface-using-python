import random
import sys
 
class ATM():
    def __init__(self, name, account_number, balance = 0,history =[]):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.history = history
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        tn=random.randint(10000, 1000000) 
        self.history.append({"Transaction number-":tn,"Deposited Rs.":self.amount}
                            )
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print("Your balance is Rs." ,self.balance, "only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print("Rs.",amount, "withdrawn successfully!")
            print("Current account balance: Rs.", self.balance)
            tn=random.randint(10000, 1000000)
            self.history.append({"Transaction number-":tn,"Withdrawn Rs.":self.amount}
                                )
            print()
            
    def transfer(self,account,amount):
        self.account = account
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print("Your balance is Rs." ,self.balance, "only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print("Rs.",amount, "transferred successfully!")
            print("Current account balance: Rs.", self.balance)
            tn=random.randint(10000, 1000000)
            self.history.append({"Transaction number-":tn,"Transferred Rs.":self.amount,"Reciever Account Number":self.account}
                                )
            print()
            
    def trans_hist(self):
        print("Last Tansactions are :-\n", self.history)
        print()

 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Deposit Money
            2. Withdraw Money
            3. Transfer Money
            4. Show Transaction History
            5. Quit
        *********************
        """)
        
        while True:
            option = int(input("Enter 1, 2, 3, 4 or 5:"))
            if option == 1:
                amount = int(input("How much you want to deposit:"))
                atm.deposit(amount)
            elif option == 2:
                amount = int(input("How much you want to withdraw:"))
                atm.withdraw(amount)
            elif option == 3:
                while True:
                    account = int(input("Enter the account number in which you want to tranfer:")) 
                    if len(str(account))==8 and account != account_number:
                        amount = int(input("How much you want to transfer:"))
                        break
                    elif account == account_number:
                        print("Same Account Number! Please try  with a different account number\n\n")
                        continue
                    else:
                        print("Wrong Account Number! Please try  logging in again\n\n")
                        continue
                atm.transfer(account,amount)
            elif option == 4:
                atm.trans_hist()
            elif option == 5:
                print(f"""
            printing receipt..............
          ******************************************
              Transaction is now complete.                          
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Rs.{self.balance}                    
              Thanks for choosing us as your bank                  
          ******************************************
          """)
                sys.exit()
            else:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                 
 
print("*******WELCOME TO PYTHON BANK ACCOUNT*******\n")
print("___________________________________________________________\n")
while True:
    print("----------ENTER YOUR DETAILS----------\n\n")
    name = input("Enter account holder name: ")
    account_number = int(input("Enter account number {Eight  digit account number e.g - XXXXXXXX}: "))
    if len(str(account_number))==8:
        break
    else:
        print("Wrong Account Number! Please try  logging in again\n\n")
        continue
print("Welcome",name,"! Account has been accessed......\n")

atm = ATM(name, account_number)
 
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   |           Visit us again!           |
    -------------------------------------
        """)
        break
    else:
        print("Wrong Command!  Enter 'y' for yes and 'n' for NO.\n")
    
