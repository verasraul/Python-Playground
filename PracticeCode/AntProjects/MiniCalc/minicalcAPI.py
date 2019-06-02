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
def divider():
    checkreq = request.method
    if checkreq == 'GET':
        divisor = float(request.args.get('divisor'))
        dividend = float(request.args.get('dividend'))
        try:
            return jsonify({"result": (dividerFunction1.divider(dividend, divisor))})
        except ZeroDivisionError:
            return make_response(jsonify({
                "error": {
                    "reason": "Cannot compute",
                    "debug": "Cannot divide by zero"
                }
            }), 400
            )

    elif checkreq == 'POST':
        content = request.get_json()
        divisor = content["divisor"]
        dividend = content["dividend"]
        try:
            return jsonify({"result": (dividerFunction1.divider(dividend, divisor))})
        except ZeroDivisionError:
            return make_response(jsonify({
                "error": {
                    "reason": "Cannot compute",
                    "debug": "Cannot divide by zero"
                }
            }), 400
            )


@app.route("/addition", methods=['POST'])
def addition():
    content = request.get_json()
    number1 = content["number1"]
    number2 = content["number2"]
    return jsonify({"result": (additionFunction1.addition(number1, number2))})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
