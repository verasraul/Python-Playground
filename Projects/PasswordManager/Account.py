__author__ = 'verasraul'

#TODO: Add tests
class Account():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def UpdatePassword(self, newPassword):
        self.password = newPassword #TODO: validate pwd
