class Account:
    passwords = {}
    def __init__(self, inputName):
        self.name = inputName

    def addPassword(self, vendor, password):
        self.passwords[vendor] = password

    def displayPassword(self):
        print(self.passwords)

    def allPasswords(self):
        return self.passwords

    def matchKeys(self, keyname):
        if keyname in self.passwords:
            return self.passwords[keyname]
        else:
            print("no password with key=",keyname)

    def getNumberOfPasswords(self):
        return len(self.passwords)







# a = Account('raul')
# a.addPassword('hotmail', 'hot')
#
# a.displayPassword()
# hotmailPassword = a.matchKeys('hotmail')
# print(hotmailPassword)
# a.matchKeys('yahoo')
# print(a.getNumberOfPasswords())