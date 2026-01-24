import requests

access_token = 'MTQ3ZGJhZDctOTY0MS00NjMyLWE1YjUtZjdhNDg5ODc3OTMwN2MzYjRiNGMtZDUz_PE93_fa936a5d-89d2-4b1b-bb50-e30cdf99ead9'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYzIyMWRhNjAtZjk0YS0xMWYwLWI1OTMtYzVlZDdjOGQwOGIw'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())