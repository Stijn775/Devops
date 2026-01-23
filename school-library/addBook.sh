#!/bin/bash

APIHOST="http://library.demo.local"
TOKEN="cisco|JcgFdnnDUJuf1ErkcTkZqB4SFW0WBgk7hpxOwltg_64"

echo "Adding new book..."

URL="$APIHOST/api/v1/books"

BOOKDATA='{
  "id": 999,
  "title": "New Book Title",
  "author": "New Author",
  "isbn": "978-0-987654-32-1",
  "pages": 250
}'

RESPONSE=$(curl -s -X POST "${URL}" \
  -H "X-API-Key: $TOKEN" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "${BOOKDATA}")

echo "Add book response:"
echo "$RESPONSE"