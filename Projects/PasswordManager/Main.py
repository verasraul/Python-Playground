__author__ = 'verasraul'

from UserManager import UsersManager

userManager = UsersManager()

def print_menu():
    print("Menu")
    print("1. Add User")
    print("6. Exit")


def main_loop():
    remainInApp = True
    while remainInApp is True:
        #remainInApp  # - this line can be removed.
        print_menu()
        menuSelection = input("What do you want to do?: ")
        if menuSelection == "1":
            print("you selected 1 which is 'Add User'")
            name = input("user name?: ")
            userManager.add_user(name)
            print("you just created a new user!!!")
            print("user="+str(userManager.users))
        elif menuSelection == "6":
            print("you chose to exit")
            remainInApp = False


if __name__ == "__main__":
    main_loop()
