__author__ = 'verasraul'
from Account import Account

#TODO: Add tests
class User():

    def __init__(self, name):
        self.name = name
        self.Accounts = {} #empty dictionary to store accounts

    def updatePassword(self, accntName, newPassword):
        account = self.Accounts[accntName]
        #todo check if the account exists
        account.UpdatePassword(newPassword)

    def addAccount(self, accountName, password):
        account = Account(accountName, password)
        self.Accounts[account.name] = account #adds accounts to account

