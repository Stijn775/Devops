#!/usr/bin/env python3

import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def deleteBook(bookId, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{bookId}", 
        headers = {
            "X-API-Key": apiKey, "accept" : "application/json"
            }
    )
    if r.status_code == 200:
        print(f"Book with ID {bookId} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delete book with ID {bookId}.")

apiKey = getAuthToken()

# Delete books range
for i in range(4, 20):
    deleteBook(i, apiKey)