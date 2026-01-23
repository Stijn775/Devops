#!/bin/bash

APIHOST="http://library.demo.local"
LOGIN="cisco"
PASSWORD="Cisco123!"

echo "Getting authentication token..."

TOKEN=$(curl -s -X POST "$APIHOST/api/v1/loginViaBasic" \
  -u "$LOGIN:$PASSWORD" \
  -H "Accept: application/json")

echo "Token response:"
echo "$TOKEN"