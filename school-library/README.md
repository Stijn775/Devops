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