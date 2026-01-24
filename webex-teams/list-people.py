import requests
import json

access_token = 'MTQ3ZGJhZDctOTY0MS00NjMyLWE1YjUtZjdhNDg5ODc3OTMwN2MzYjRiNGMtZDUz_PE93_fa936a5d-89d2-4b1b-bb50-e30cdf99ead9'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'stijn.dekeyser@student.odisee.be'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

#####################################
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS83ZDFkMjgyNi1mN2JiLTRlYzktODQ2ZC1iZjkxZTZjZDUzMGU'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))