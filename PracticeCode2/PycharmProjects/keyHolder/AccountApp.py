import AccountClassHolder
# from AccountClassHolder import Account

# Function that stores the key from user input into the empty dictionary defined above
def keyname():
    global account
    accName = input("Enter Account Name: ")
    account = AccountClassHolder.Account(accName)
    vendor = input("Enter vendor: ")
    value = input("Enter Password: ")
    account.addPassword(vendor, value)
    initiate()


# Prompts usesr to search for stored passwords
def searchPrompt():
    prompt = input("Would you like to search for stored Passwords? Y/N ")
    if prompt.upper() == 'Y':
        return searchKey()
    elif prompt.upper() == 'N':
        print("Thanks, program will now close")
        quit()
    else:
        print("This is not a valid option! Please try again")
        return searchPrompt()


# Function that searches for existing keys
def searchKey():
    sKey = input("Enter name of vendor whose password you would like to view: ")
    password = account.matchKeys(sKey)
    print(password)
    return initiate()


# Function that starts the program, first rule of business
def initiate():
    start = input("Would you like to save a new password? Y/N ")
    if start.upper() == 'Y':
        print("Ok")
        return keyname()
    elif start.upper() == 'N':
        print("ok")
        return searchPrompt()
        # quit()
    else:
        print("This is not a valid option! Please try again")
        return initiate()



initiate()
