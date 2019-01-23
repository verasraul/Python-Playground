from flask import Flask
from flask import request
from AccountClassHolder import Account


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/account/create", methods=['POST'])
def createAccount():
    data = request.data
    print(data)
    global account
    account = Account(str(data))
    return "acount successfully created with name="+account.name

@app.route("/account/passwords")
def getAllPasswords():
    # return "function to get all passwords under construction!!!!"
    return str(account.allPasswords())

@app.route("/account/password")
def addPassword():
    account.addPassword('hotmail', 'hot') #TODO: get this from web
    return "successfully added password"

if __name__ == "__main__":
    app.run()
