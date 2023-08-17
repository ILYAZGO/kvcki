import requests
#from variables import *

URL = "https://api.stand.imot.io"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def get_tok():
    data = {
        'username': '4adminIM',
        'password': 'Qaz123wsX',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }
    result = requests.post(url=URL + "/token", headers=headers, data=data)
    return result

token = get_tok().json()
bearer = token['token_type'].capitalize()
access_token = token['access_token']


headers1 = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': bearer+" "+access_token,
}

def create_user():
    data = {'role': 'user',
            'login': 'qwe',
            'name': 'qwe',
            'email': '',
            'comment': '',
            'password': 'qwe'}
    result = requests.post(url=URL + "/user", headers=headers1, json=data)

    return result

print (create_user().text)
print(create_user().json())
