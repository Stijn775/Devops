# School Library API Project

## Overview
This project contains Python and Bash scripts to interact with a School Library REST API. It demonstrates all 4 main HTTP methods (GET, POST, PUT, DELETE) for API calls.

## HTTP API Methods

### GET - ophalen data
- Haalt bestaande gegevens op
- Veilig en idempotent
- Gebruikt query parameters voor filters

### POST - nieuwe data toevoegen
- Voegt een nieuwe resource toe
- Gegevens in request body
- Retourneert meestal het nieuw aangemaakte object

### PUT - Data updaten
- Vervangt een bestaande resource
- Vereist volledige object data
- Idempotent

### DELETE - Data verwijderen
- Verwijdert een resource
- Geen body nodig
- Retourneert status

## Bestandbeschrijving

### Python Scripts

| Bestand | Functie | HTTP Method |
|---------|---------|-------------|
| `get_token.py` | Authentificatie - krijgt API token via Basic Auth | POST |
| `getbooks.py` | Haalt alle boeken op met optionele ISBN | GET |
| `getbookbyid.py` | Haalt een specifiek boek op via ID | GET |
| `addBook.sh` | Voegt nieuw boek toe via API | POST |
| `updatebook.py` | Update bestaand boek | PUT |
| `delete-books.py` | Verwijdert boeken | DELETE |
| `add100RandomBooks.py` | Voegt 100 random boeken toe (bulk) | POST |

### Bash Scripts

| Bestand | Functie |
|---------|---------|
| `gettoken.sh` | Bash versie voor token ophalen |
| `getBooks.sh` | Bash versie voor alle boeken ophalen |
| `Getbookbyid.sh` | Bash versie voor boek per ID ophalen |
| `addBook.sh` | Bash versie voor boek toevoegen |
| `updatebook.sh` | Bash versie voor boek updaten |
| `deleteBook.sh` | Bash versie voor boek verwijderen |

## Authentificatie

De API vereist een token die verkregen wordt via Basic Authentication:
- **Endpoint:** `POST /api/v1/loginViaBasic`
- **Login:** cisco
- **Password:** Cisco123!
- Token wordt gebruikt in header: `X-API-Key: <token>`

## Gebruik

### Python voorbeelden:
```bash
python3 get_token.py              # Token ophalen
python3 getbooks.py               # Alle boeken ophalen
python3 getbookbyid.py <id>       # Boek per ID ophalen
python3 addBook.sh                # Nieuw boek toevoegen
python3 updatebook.py             # Boek updaten
python3 delete-books.py           # Boeken verwijderen
```

### Bash voorbeelden:
```bash
bash gettoken.sh                  # Token ophalen
bash getBooks.sh                  # Alle boeken ophalen
bash addBook.sh                   # Nieuw boek toevoegen
```

## API Host
- **URL:** http://library.demo.local

## Vereisten
- Python 3.x met `requests` library
- Bash (voor bash scripts)
- curl (voor curl commando's in bash scripts)
- Netwerk verbinding met library.demo.local

---

## Curl Commando Uitleg - Update Book

### Volledig Commando
```bash
RESPONSE=$(curl -s -X PUT "${URL}" \
  -H "X-API-Key: $TOKEN" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d "${BOOKDATA}")
```

### Onderdeel Details

#### `RESPONSE=$(...)`
- Slaat de output van het curl commando op in de variabele `RESPONSE`
- De `$(...)` syntax voert het commando uit en vangt de output

#### `curl`
- Command line tool voor het maken van HTTP requests
- Ondersteunt alle HTTP methodes (GET, POST, PUT, DELETE, etc.)

#### `-s` (silent mode)
- Onderdrukt de voortgangsbalk en error berichten
- Laat alleen de daadwerkelijke response data zien
- Houdt de output schoon voor verdere verwerking

#### `-X PUT`
- Specificeert de HTTP methode: PUT
- PUT wordt gebruikt om een bestaande resource te updaten/vervangen
- Alternatief: `-X GET`, `-X POST`, `-X DELETE`

#### `"${URL}"`
- De volledige URL naar de API endpoint
- In dit geval: `http://library.demo.local/api/v1/books/{BOOK_ID}`
- De `${}` syntax zorgt voor variabele expansie in bash

#### `-H "X-API-Key: $TOKEN"`
- Voegt een custom HTTP header toe: `X-API-Key`
- Bevat de authenticatie token verkregen via `get_token.py` of `gettoken.sh`
- API gebruikt deze header om te verifiëren of je geautoriseerd bent
- Formaat: `-H "Header-Name: Header-Value"`

#### `-H "accept: application/json"`
- Vertelt de server welk response formaat je wilt ontvangen
- `application/json` = je wilt JSON data terug
- Server kan hiermee de juiste content-type voor de response kiezen
- Andere opties: `text/html`, `application/xml`, etc.

#### `-H "Content-Type: application/json"`
- Vertelt de server in welk formaat je data **stuurt**
- `application/json` = je stuurt JSON data in de request body
- Server weet hierdoor hoe de body data te parsen
- Essentieel voor POST en PUT requests met data

#### `-d "${BOOKDATA}"`
- Stuurt data mee in de request body (data/payload)
- Bevat de JSON data met boek informatie die geüpdatet moet worden
- Bij PUT: volledige object data (alle velden)
- Bij POST: nieuwe object data
- GET en DELETE hebben meestal geen body data
- Voorbeeld BOOKDATA:
  ```json
  {
    "id": 123,
    "title": "Updated Title",
    "author": "Updated Author",
    "isbn": "978-0-123456-78-9",
    "pages": 350
  }
  ```

#### `\` (backslash)
- Line continuation character in bash
- Maakt lange commando's leesbaarder door ze over meerdere regels te spreiden
- Elk `\` aan het einde van een regel betekent: "dit commando gaat verder op de volgende regel"

### Complete Flow

1. **curl** start het HTTP request
2. **-s** zorgt voor schone output (geen progress bar)
3. **-X PUT** zegt: dit is een UPDATE operatie
4. **"${URL}"** geeft aan WAAR het request naartoe gaat
5. **-H "X-API-Key: $TOKEN"** authenticatie/autorisatie
6. **-H "accept: application/json"** vraagt om JSON response
7. **-H "Content-Type: application/json"** vertelt dat we JSON sturen
8. **-d "${BOOKDATA}"** bevat de daadwerkelijke data om te updaten
9. **RESPONSE=$(...)** vangt het antwoord van de server op

### Wat gebeurt er?

1. curl maakt een HTTPS/HTTP connectie met de server
2. Stuurt een PUT request naar de opgegeven URL
3. Voegt de 3 headers toe aan het request
4. Stuurt de JSON data in de body
5. Server verwerkt het request (update het boek in de database)
6. Server stuurt een response terug (meestal het geüpdatete object + status code)
7. curl ontvangt de response
8. Response wordt opgeslagen in de RESPONSE variabele
9. Je kunt nu `echo "$RESPONSE"` gebruiken om het resultaat te zien

### HTTP Status Codes bij PUT

- **200 OK** - Succesvol geüpdatet
- **204 No Content** - Succesvol geüpdatet, geen data terug
- **400 Bad Request** - Ongeldige data gestuurd
- **401 Unauthorized** - Geen of ongeldige token
- **404 Not Found** - Boek met dit ID bestaat niet
- **500 Internal Server Error** - Server fout