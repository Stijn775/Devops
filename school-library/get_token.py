#!/usr/bin/env python3
import requests

login_url = "http://library.demo.local/api/v1/loginViaBasic"

LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(
            login_url, 
            auth=(LOGIN, PASSWORD),
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        exit(1)
    
    token = data.get("token")
    if not token:
        print("Token not found in the response.")
        exit(1)
    
    return token

if __name__ == "__main__":
    token = getAuthToken()
    print(f"Token: {token}")