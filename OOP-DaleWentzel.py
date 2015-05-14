# OOP ASSIGNMENT SHELL (Bank Account Manager)
f=open("ATM_Transaction_Log.txt", "w")
#Your code here for 3 classes
class Accounts(object):
    def __init__(self,Balance):
        self.Balance=Balance
        print ("Your current balance is: %s" % (self.Balance))
        output="Initiated ATM. Initial balance: %s" +"\n" %(self.Balance)
        f.write (output)
        
    def Deposit(self):
        amount= int(input("How much money will you deposit? "))
        self.Balance=amount+self.Balance
        print ("Your new balance is %s" % (self.Balance))
        output2="Deposited $%s. New balance of %s." + "\n"%(amount,self.Balance)
        f.write(output2)
        run=0
    def Withdraw(self):
        amount= int(input("How much money will you withdraw?"))
        if amount>self.Balance:
            print ("Insufficient Funds")
            f.write("Overdrawn. Transaction aborted." + "\n")
            run=0
        else:
            self.Balance= self.Balance-amount
            print ("your new balance is %s " % (self.Balance))
            f.write("Withdrew %s. New Balance of %s" + "\n" %(amount,self.Balance))
            run=0
    def CheckBalance(self):
        print ("Your balance is: %s" % (self.Balance))
        f.write ("Checked Balance. Current Balance of %s." + "\n" %(self.Balance))
        run=0
class Checking(Accounts):
    def With_draw(self):
        amount= int(input("How much money will you withdraw?"))
        if amount>self.Balance-100:
            print("Insufficient funds")
            f.write("Overdrawn. Transaction aborted." + "\n")
        else:
            self.Balance= self.Balance-amount
            print ("your new balance is %s " % (self.Balance))
            f.write("Withdrew %s. New Balance of %s" + "\n" %(amount,self.Balance))
            run=0
        
class Savings(Accounts):
    def Interest(self):
        time=int(input("How many years has interest been accumulating? "))
        interest= time*.01*self.Balance
        calculateinterest=self.Balance+interest
        print ("You have earned %s bringing your balance to %s" % (interest,calculateinterest))
        f.write("Accumulated $%s in interest. New Balance of %s" +"\n" % (interest,calculateinterest))
        run=0

run=0
print("Welcome to Helmsworth Accounting's ATM")
def Main():
    accountType = int(input("What type of account? 1:Savings; 2:Checking?"))
    if accountType == 1:
        accountPicked = Savings(1500)
        action= int(input("""What would you like to do? 1:Deposit; 2:Withdraw; 3:Check Balance; 4:Interest """))
        if action==1:
            accountPicked.Deposit()
            run=1
        elif action==2:
            accountPicked.Withdraw()
            run=1
        elif action==3:
            accountPicked.CheckBalance()
            run=1
        else:
            accountPicked.Interest()
            run=1
    
    elif accountType == 2:
        accountPicked = Checking(1000)
        action= int(input("""What would you like to do? 1:Deposit; 2:Withdraw; 3:Check Balance """))
        if action==1:
            accountPicked.Deposit()
            run=1
        elif action==2:
            accountPicked.With_draw()
            run=1
        else:
            accountPicked.CheckBalance()
            run=1


    #Your code here - loop asking the user what they want to do


while run==0:
    Main()
    again= int(input("Would you like to make another transaction? 1:yes; 2:no"))
    if again ==1:
        Main()
        run=2
    else:
        run=3
        print ("Have a nice day. Come back soon.")
f.close()
