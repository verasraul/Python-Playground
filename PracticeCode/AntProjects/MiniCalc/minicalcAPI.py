__author__ = 'verasraul'
'''
Flask API for divider/addition functions.

This will allow the functions to run on the browser.
'''

# import Flask class from flask module to create REST api.
from flask import Flask, jsonify, request, make_response

# import divider and addition modules.
import dividerFunction1
import additionFunction1

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"result": "Welcome Home!"})


@app.route("/divider", methods=['POST', 'GET'])
def zError():
    '''Grab argument requests from URL endpoint'''
    divisor = request.args.get('divisor')
    dividend = request.args.get('dividend')
    # Accept ZeroDivision error and return customized error message in JSON format'''
    try:
        return jsonify({"result": (dividerFunction1.divider(dividend, divisor))})
    except ZeroDivisionError as error:
        return make_response(jsonify({
            "error": {
                "reason": "Cannot compute",
                "debug": "Cannot divide by zero"
            }
        }), 400
        )


def divider():
    checkreq = request.method
    if checkreq == 'GET':
        zError(divisor=" ", dividend=" ")


    elif checkreq == 'POST':
        content = request.get_json()


@app.route("/addition", methods=['POST'])
def addition():
    content = request.get_json()
    number1 = request.args.get('number1')
    number2 = request.args.get('number2')
    return jsonify({"result": (additionFunction1.addition(number1, number2))})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
