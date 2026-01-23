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

def updateBook(apiKey, bookId: str, bookData: dict):
    headers = {"X-API-Key": apiKey, "Content-Type": "application/json"}
    r = requests.put(f"{APIHOST}/api/v1/books/{bookId}", headers=headers, json=bookData, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    p = argparse.ArgumentParser(description="Update a book in library API")
    p.add_argument("bookId", help="The ID of the book to update")
    args = p.parse_args()

    # Voorbeeld update data
    updateData = {
        "title": "Updated Book Title",
        "author": "Updated Author",
        "isbn": "978-0-123456-78-9",
        "pages": 350
    }

    apiKey = getAuthToken()
    updatedBook = updateBook(apiKey, args.bookId, updateData)
    print(json.dumps(updatedBook, indent=2))

if __name__ == "__main__":
    main()