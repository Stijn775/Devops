#!/bin/bash

APIHOST="http://library.demo.local"
LOGIN="cisco"
PASSWORD="Cisco123!"

TOKEN=$(curl -s -X POST "$APIHOST/api/v1/loginViaBasic" \
  -u "$LOGIN:$PASSWORD" \
  -H "Accept: application/json" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)

echo "Getting book with ID: $1"

BOOK_ID="$1"
URL="$APIHOST/api/v1/books/${BOOK_ID}"

RESPONSE=$(curl -s -X GET "${URL}" \
  -H "X-API-Key: $TOKEN" \
  -H "accept: application/json")

echo "Book response:"
echo "$RESPONSE"