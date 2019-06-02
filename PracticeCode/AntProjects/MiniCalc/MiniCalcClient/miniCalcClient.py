__author__ = 'verasraul'
import requests

# response = requests.get("http://localhost:5000/")
# body = response.content

def addition(numb1, numb2):
    data = {"number1": numb1,"number2": numb2}
    addition_request = requests.post("http://localhost:5000/addition", json=data)
    site_response = addition_request.json()
    return site_response['result']


def divider(divisor, dividend):
    data = {"divisor": float(divisor) ,"dividend": float(dividend)}
    divider_request = requests.post("http://localhost:5000/divider", json=data)
    site_response = divider_request.json()
    if divider_request.status_code == 400:
        raise Exception(site_response['error']['debug'])
    else:
        return site_response['result']



