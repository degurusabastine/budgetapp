import random
import datetime
 
class Account:
    
    def __init__(self, id, balance = 0, annualInterestRate = 3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate
 
    def getPin(self):
        return self.pin
 
    def getBalance(self):
        return self.balance
 
    def getAnnualInterestRate(self):
        return self.annualInterestRate
 
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount
        
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

    def main():
        accounts = []
    for i in range(1000, 9999):
        account = Account (i, 0)
        accounts.append(account)
        
    while True:
        username = input ("USERNAME:")
        pin = int(input("nEnter account pin: "))
        while pin <1000 or pin > 9999:
            pin = int(input("\nInvalid ID or USERNAME.. Try-again: "))
            
            while True:
                print("welcome" + username.upper() + "*" * 50 + "login time:" + str(datetime.datetime.now()))
                print(" " * 100)
                
                print("\n1 - Withdrawal \t 2 - Viewbalance \t 3 - Deposit \t 4 - Comment/Exit ")
                choice = int(input("Enter your selection: "))
                
                for acc in accounts:
                    if acc.getpin() == pin:
                        accountObj = acc
                        break
                    
                    if choice == 2:
                        print(accountObj.getBalance())
                    elif choice == 1:
                        amt = float(input("\Enter amount to withdraw: "))
                        ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(ver_withdraw))   
                    else:
                        break
                    if amt < accountObj.getBalance():
                        accountObj.withdraw(amt)
                        print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
                    else:
                        print("\nInsufficient funds you can't carry out transaction: " + str(accountObj.getBalance()) + "n")
                        print("\nPlease make a deposit.")
                    elif: choice == 3:
                        amt = float(input("\Enter amount to deposit: "))
                        ver_deposit = input("Is this the correct amount, Yes or No ? " + str(ver_deposit))
                        if ver_deposit == "Yes":
                            accountObj.deposit(amt)
                            print("\nUpdated Balance:  " + str(accountObj.getBalance()) + " n")")
                        else:
                        break
                    if amt > accountObj.getBalance():
                        accountObj.deposit(amt)
                        print("\nUpdated Balance: " + str(accountObj.getBalance()) + " n")
                    else:
                    break
                    elif choice == 4:
                    print("Thanks for choosing us as your bank")
                    print("fill in complain/suggestions below: ")
                    complain = input("COMMENT/COMPLAIN: ")
                    print("Thanks for your comment Mr/Mrs " + username + "we will look into it")
                    exit()
                    
                    else:
                    print("\nThat's an invalid choice."
main()
                    
                    
                    
                    