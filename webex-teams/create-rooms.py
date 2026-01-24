import requests

access_token = 'MTQ3ZGJhZDctOTY0MS00NjMyLWE1YjUtZjdhNDg5ODc3OTMwN2MzYjRiNGMtZDUz_PE93_fa936a5d-89d2-4b1b-bb50-e30cdf99ead9'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())