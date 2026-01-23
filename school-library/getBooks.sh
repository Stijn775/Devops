includeISBN="true"
URL="http://library.demo.local/api/v1/books?includeISBN=${includeISBN}"

BOOKLIST=$(curl -s -X GET "${URL}" -H "accept: application/json")

echo "$BOOKLIST"