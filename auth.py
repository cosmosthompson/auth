#register
# - firstname, lastname, password, email
# - generaten user account

#login
# - account number and password

#bank operations


# Initializing the system
import random
from datetime import datetime

currentDateTime = datetime.now()

database = {
    2082224970: ["Cosmos" , "Thompson" , "cosmosthompson@gmail.com" , "cosmosPassword"]
    }


def init():

    
    print("Welcome to bankPHP")

    

    haveAccount = int(input("Do you have account with us: 1(yes) 2(no) \n"))

    if(haveAccount == 1):
                
        login()
    elif(haveAccount == 2):
                
        register()
    else:
        print("You have selected invalid option")
    init()


def login():

    print("******* Login ******")
   
    accountNumberFromUser = input("What is your account number? \n")

    isValidAccountNumber = accountNumberValidation(accountNumberFromUser)

    if isValidAccountNumber:

        password = input("What is your password \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == int(accountNumberFromUser)):
                if(userDetails[3] == password):
                    bankoperation(userDetails)
                    isLoginSuccessful = True
                else:
                    print("Invalid account or passoword")
                    login()

    else:
        init()


def accountNumberValidation(accountNumber):
  
    if accountNumber:

        if(len(str(accountNumber)) == 10):

            try:
                int(accountNumber)
                return True
            except ValueError:
                print("Invalid Account Number, account number should be integer")
                return False
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Account Number cannot be less or more than 10 digits")
            return False

    else:
        print("Account Number is a required field")
        return False


    

def register():

    print("******** Register ********")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    try:
         accountNumber = generationAccountNumber()
    
    except ValueError:
        print("Account generation failed due to internet connection failure")
        init()


   

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account has been created")
    print("== ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ====== ===== ===")

    login()


def bankoperation(user):

    print("Welcome %s %s " % (user[0], user[1]))
    print("Login Date %s" % currentDateTime)


    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaint (4) Logout (5) Exit \n "))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        complaint()
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else:
        
        print("Invalid option selected")
        bankoperation(user)


def withdrawalOperation():
    print("Withdrawal")
    cash = input("How much would you like to withdraw: \n")
    print("Please take your cash: %s " %cash)
    anotherTransaction()


def depositOperation():
    print("Deposit Operations")
    deposit = input("How much would you like to deposit: \n")
    print("Your Current balance is: %s " %deposit)
    anotherTransaction()
   
   
def complaint():
    print("complaint")
    compliant = input("Please what issue will you like to report?: \n")
    print("Thank you for contacting us. ")

def anotherTransaction():
    print("Hi would you like to do another transaction")
    select = int(input("Press 1 to continue\nPress 2 to logout.\n"))
    if (select == 1):
        do = int(input("Welcome back for another transaction\n (1) Deposit\n (2) Withdrawal\n (3) Complaint\n"))
        if (do == 1):
            depositOperation()
        elif (do == 2):
            withdrawalOperation()
        elif (do == 3):
                complaint()
        else:
            print("Invalid option")
            anotherTransaction()

    elif(select == 2):
        print("Bye, thank you for coming")
        logout()
    else:
        print("Invalid input")
        anotherTransaction()

def generationAccountNumber():
    return random.randrange(1111111111,9999999999)


def setCurrentBalance(userDetails, balance):
    userDetails[4] = balance



def getCurrentBalance(userDetails):
    return userDetails[4]



def logout():
    login()




#### ACTUAL BANKING SYSTEM ####


init()






