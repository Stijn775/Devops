#!/usr/bin/env python3
"""
Virtual Environment Experiment Script
Demonstrates working with venv and making API calls
"""

import requests
import json

def get_public_api_data():
    """
    Fetch data from a public API as an experiment
    Using the JSONPlaceholder API (free, no auth needed)
    """
    print("=" * 50)
    print("VENV EXPERIMENT - API Call Test")
    print("=" * 50)
    
    # Test 1: Get user data from JSONPlaceholder API
    print("\n1. Fetching user data...")
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        user_data = response.json()
        print(f"✓ User: {user_data['name']}")
        print(f"✓ Email: {user_data['email']}")
        print(f"✓ Company: {user_data['company']['name']}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error: {e}")
        return False
    
    # Test 2: Get posts
    print("\n2. Fetching posts...")
    url = "https://jsonplaceholder.typicode.com/posts?userId=1"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        posts = response.json()
        print(f"✓ Found {len(posts)} posts")
        print(f"✓ First post title: {posts[0]['title']}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error: {e}")
        return False
    
    # Test 3: Pretty print JSON
    print("\n3. Full user data (JSON format):")
    print(json.dumps(user_data, indent=2))
    
    print("\n" + "=" * 50)
    print("✓ All tests passed!")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    success = get_public_api_data()
    exit(0 if success else 1)
