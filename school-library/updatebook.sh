#!/bin/bash

APIHOST="http://library.demo.local"
TOKEN="cisco|JcgFdnnDUJuf1ErkcTkZqB4SFW0WBgk7hpxOwltg_64"

echo "Updating book with ID: $1"

BOOK_ID="$1"
URL="$APIHOST/api/v1/books/${BOOK_ID}"

BOOKDATA='{
  "id": '$BOOK_ID',
  "title": "je moeder",
  "author": "Updated Author",
  "isbn": "978-0-123456-78-9",
  "pages": 350
}'

RESPONSE=$(curl -s -X PUT "${URL}" \
  -H "X-API-Key: $TOKEN" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "${BOOKDATA}")

echo "Update response:"
echo "$RESPONSE"