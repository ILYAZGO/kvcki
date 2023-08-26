import requests

headers_for_get_token = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

data = {
        'username': '4adminIM',
        'password': 'Qaz123wsX',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }

get_token = requests.post(url="https://api.stand.imot.io" + "/token", headers=headers_for_get_token, data=data)

print (get_token.text)
print (get_token.json())

token = get_token.json()
bearer = token['token_type'].capitalize()
access_token = token['access_token']

print(bearer)
print(access_token)