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

def getBookById(apiKey, bookId: str):
    headers = {"X-API-Key": apiKey, "Accept": "application/json"}
    r = requests.get(f"{APIHOST}/api/v1/books/{bookId}", headers=headers, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    p = argparse.ArgumentParser(description="Get a book by ID from library API")
    p.add_argument("bookId", help="The ID of the book to retrieve")
    args = p.parse_args()

    apiKey = getAuthToken()
    book = getBookById(apiKey, args.bookId)
    print(json.dumps(book, indent=2))

if __name__ == "__main__":
    main()