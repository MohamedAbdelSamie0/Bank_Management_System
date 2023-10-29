#BANK MANAGEMENT SYSTEM
import csv
import fileinput
import sys


def deposit():#function that adds in the amount using the account number as a key
    #opening the csv file in read mode
    with open("CSV data file.csv") as f:
        ro=csv.reader(f)
        rows=[]
        deposit_amount=int(input("enter deposit amount: "))
        for rec in ro:
            rows.append(rec)
        rows[account_number][2]=int(rows[account_number][2])+deposit_amount
    #rewriting the csv file with the updated value in the amount column
    with open("CSV data file.csv",'w') as f:
        wo=csv.writer(f,lineterminator='\n')
        wo.writerows(rows)

def withdraw():#function to make a deduction in the amount using the account number as a key
    #opening the csv file in read mode
    with open("CSV data file.csv") as f:
        ro=csv.reader(f)
        rows=[]
        withdraw_amount=int(input("enter the amount to withdraw: "))
        for rec in ro:
            rows.append(rec)
        rows[account_number][2]=int(rows[account_number][2])-withdraw_amount
    #rewriting the csv file with the updated value in the amount column
    with open("CSV data file.csv",'w') as f:
        wo=csv.writer(f,lineterminator='\n')
        wo.writerows(rows)

def balance():#function that outputs the balance amount present in csv file
    #opening the csv file in read mode
    with open("CSV data file.csv","r") as f:
        #the reader object
        csv_dict_reader = csv.DictReader(f)
        #looping the rows in reader object to find the amount corresponding to entered account number
        for row in csv_dict_reader:
            AN=int(row['account number'])
            if AN == account_number:
                print("\ncurrent balance:")
                print(row['amount'])

def GBM():#function that outputs a customized goodbye message
    #opening the csv file in read mode to print out the name corresponding to the account number entered
    with open("CSV data file.csv","r") as f:
        csv_dict_reader = csv.DictReader(f)
    
        for row in csv_dict_reader:
            AN=int(row['account number'])
            if AN == account_number:
               print("\ngoodbye")
               print(row['full name'])


#main program

while True:#infinitly looping the program untill user chooses to exit
    print("\n           Welcome to our bank")
    
    #validation checks to limit the user input to an acceptable range
    while True:
        try:
            n=account_number=int(input("please enter your account number: ")) #take the account number as an input from the user and only accept whole numbers (integers)
            count=0
            while (n>0 and n<9):
                count = count+1
                n=n//10
            else:
                if(count==1):
                    break
                else:
                    print("account number not correct, try again")
        except:
            print("account number not correct, try again")

    #opening the csv file in read mode to get the corresponding name of the typed in account number
    with open("CSV data file.csv","r") as f:

        csv_dict_reader = csv.DictReader(f)

        for row in csv_dict_reader:
            AN=int(row['account number'])
            if AN == account_number:
                print("\nWelcome")
                print(row['full name'])

    #menu of options to choose the required operation from
    while True:
        print("\nChoose the required operation")

        print("\n1- balance inquiry")
        print("2- make a deposit")
        print("3- withdraw money")
        print("4- exit")
        ch=int(input("\nenter your choice: "))
        while True:
                if ch==1:
                    balance()
                    break
                if ch==2:
                    deposit()
                    break
                if ch==3:
                    withdraw()
                    break
                if ch==4:
                    GBM()
                    sys.exit()

        while(ch!=4):
            print("\nMake another operation?")
            Ex=input("[Y/N]\n")
            if(Ex=='N' or Ex=='n'):
                GBM()
                sys.exit()
            else:
                break
