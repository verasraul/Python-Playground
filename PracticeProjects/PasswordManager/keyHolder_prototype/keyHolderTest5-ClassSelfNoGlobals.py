
password = {}



class KeyHolder:
    # def __init__(self):
    #     self.name = "bob"

    # Function that stores the key from user input into the empty dictionary defined above
    def keyname(self):
        print("Enter the password you would like to store")
        key = input("Enter Account Name: ")
        value = input("Enter Password: ")
        password[key] = value
        self.initiate()

    # Prompts usesr to search for stored passwords
    def searchPrompt(self):
        Prompt = input("Would you like to search for stored Passwords? Y/N ")
        if Prompt.upper() =='Y':
            return self.searchKey()
        elif Prompt.upper() == 'N':
            print("Thanks, program will now close")
            quit()
        else:
            print("This is not a valid option! Please try again")
            return self.searchPrompt()

    # Function that searches for existing keys
    def searchKey(self):
        sKey = input("Enter name of account you would like to view: ")
        if sKey in password:
            print(password[sKey])
            return self.initiate()
        elif sKey not in password:
            print("There is no such password stored")
            return self.initiate()

    # def getName(self):
    #     print("my name="+self.name)
    #     return self.name

    # Function that starts the program, first rule of business
    def initiate(self):
        print("calling getName() before anything...")
        # self.getName()

        start = input("Would you like to save a new password? Y/N ")
        if start.upper() == 'Y':
            print("Ok")
            return self.keyname()
        elif start.upper() == 'N':
            print("ok")
            return self.searchPrompt()
            # quit()
        else:
            print("This is not a valid option! Please try again")
            return initiate()


holder = KeyHolder()

holder.initiate()
