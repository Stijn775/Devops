#!/bin/bash

BOOK_ID="$1"
URL="http://library.demo.local/api/v1/books/${BOOK_ID}"

RESPONSE=$(curl -s -X DELETE "${URL}" -H "accept: application/json")

echo "$RESPONSE"