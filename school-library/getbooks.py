#!/usr/bin/env python3
import sys
import argparse
import json
import requests

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    r = requests.post(f"{APIHOST}/api/v1/loginViaBasic", auth=(LOGIN, PASSWORD), timeout=10)
    r.raise_for_status()
    token = r.json().get("token")
    if not token:
        raise Exception(f"No token in auth response: {r.text}")
    return token

def getBooks(apiKey, includeISBN: bool = True):
    params = {"includeISBN": str(includeISBN).lower()}
    headers = {"X-API-Key": apiKey, "Accept": "application/json"}
    r = requests.get(f"{APIHOST}/api/v1/books", headers=headers, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    p = argparse.ArgumentParser(description="Get all books from library API")
    p.add_argument("--includeISBN", action="store_true", help="Include ISBNs in the response")
    p.add_argument("--no-includeISBN", dest="includeISBN", action="store_false",
                   help="Do not include ISBNs in the response")
    p.set_defaults(includeISBN=True)
    args = p.parse_args()

    apiKey = getAuthToken()
    books = getBooks(apiKey, includeISBN=args.includeISBN)
    print(json.dumps(books, indent=2))

if __name__ == "__main__":
    main()