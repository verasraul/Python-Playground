


password = {}


#Function that stores the key from user input into the empty dictionary defined above
def holder():
    print("Enter the password you would like to store")
    key = input("Enter Account Name: ")
    value = input("Enter Password: ")
    password[key] = value
    initiate()

#Function to allow user to search for stored passwords 
def searchKeys():
    searchPrompt = input("Would you like to search for stored Passwords? Y/N ")
    searchKey = input("Enter name of account you would like to view: ")
    #print (searchPrompt)
    if searchPrompt.upper() == 'Y':
        print(password[searchKey])
    elif searchPrompt.upper() =='N':
        print ("Thanks, program will now close")
        quit()
    searchKeys()

#Function that starts the program, first rule of business
def initiate():
    start = input("Would you like to save a new password? Y/N ")
    if start.upper() == 'Y':
        print("Ok")
        holder()
    elif start.upper() == 'N':
        print("ok")
        searchKeys()
        #quit()
    else:
        print("This is not a valid option! Please try again")
        return initiate()
        

initiate()
#print(password)
