# Webex Teams API Project

## Overzicht
Dit project bevat Python scripts om te interageren met de Webex Teams (Cisco Webex) REST API. Je kunt rooms beheren, berichten versturen, mensen toevoegen en meer.

## Vereisten

- **Python 3.x** met `requests` library
- **Webex Teams Account**
- **Personal Access Token** van Webex Developer Portal
- **Internet verbinding** naar Webex APIs

## Setup

### 1. Personal Access Token Ophalen

1. Ga naar https://developer.webex.com/
2. Login met je Webex account
3. Klik op je **profiel** in de rechterbovenhoek
4. Klik **"Copy Personal Access Token"**
5. Bewaar dit token veilig

### 2. Token in Scripts Plaatsen

Voeg je token in alle scripts in:
```python
access_token = 'jouw_token_hier'
```

**Beter: Gebruik environment variabelen voor veiligheid:**
```bash
export WEBEX_TOKEN='jouw_token_hier'
```

## Bestandbeschrijving

### Basis Scripts

| Bestand | Functie | HTTP Method |
|---------|---------|-------------|
| `authentication.py` | Controleert je token en haalt gebruikersinfo op | GET |
| `get_token.sh` | Haalt token op via OAuth2 flow (bash) | POST |

### Room Management

| Bestand | Functie | HTTP Method |
|---------|---------|-------------|
| `list-rooms.py` | Toont alle beschikbare rooms | GET |
| `create-rooms.py` | Maakt een nieuwe room aan | POST |
| `get-room-details.py` | Haalt details van een specifieke room op | GET |

### Berichten & Content

| Bestand | Functie | HTTP Method |
|---------|---------|-------------|
| `create-markdown-message.py` | Stuurt een bericht met markdown formatting | POST |

### Mensen & Memberships

| Bestand | Functie | HTTP Method |
|---------|---------|-------------|
| `list-people.py` | Toont alle personen in je org | GET |
| `list-memberships.py` | Toont members van een room | GET |
| `create-membership.py` | Voegt persoon toe aan room | POST |

### Paginatie

| Bestand | Functie |
|---------|---------|
| `pagination.py` | Voorbeeld van paginatie in API calls |
| `pagination-next.py` | Geavanceerde paginatie |

## API Endpoints

Basis URL: `https://webexapis.com/v1/`

### Veel gebruikte endpoints:

| Endpoint | Beschrijving |
|----------|-------------|
| `/people/me` | Huidige gebruiker info |
| `/rooms` | Alle rooms |
| `/messages` | Berichten |
| `/memberships` | Room members |
| `/attachmentActions` | Attachment actions |

## Authentificatie

Alle requests vereisen een `Authorization` header:
```python
headers = {
    'Authorization': 'Bearer <access_token>',
    'Content-Type': 'application/json'
}
```

## Voorbeelden

### 1. Je Eigen Info Ophalen
```bash
python3 authentication.py
```

### 2. Alle Rooms Weergeven
```bash
python3 list-rooms.py
```

### 3. Nieuwe Room Aanmaken
```bash
python3 create-rooms.py
```

### 4. Bericht Sturen
```bash
python3 create-markdown-message.py
```

### 5. Persoon Toevoegen aan Room
```bash
python3 create-membership.py
```

## HTTP Methoden

| Methode | Doel |
|---------|------|
| `GET` | Data ophalen |
| `POST` | Nieuw item maken |
| `PUT` | Item updaten |
| `DELETE` | Item verwijderen |

## Response Codes

| Code | Betekenis |
|------|-----------|
| 200 | OK - Succesvol |
| 201 | Created - Nieuw item aangemaakt |
| 400 | Bad Request - Ongeldig request |
| 401 | Unauthorized - Token invalide |
| 403 | Forbidden - Geen permissie |
| 404 | Not Found - Resource niet gevonden |

## Troubleshooting

### Token Errors (401)
- Check of token correct is gekopieerd
- Token kan verlopen zijn - haal een nieuwe op
- Check of Bearer prefix correct is

### Room Not Found (404)
- Zorg dat room ID correct is
- Gebruik `list-rooms.py` om rooms te vinden

### Rate Limiting
- Webex API heeft rate limits
- Voeg vertraging toe tussen requests:
```python
import time
time.sleep(1)  # 1 seconde wachten
```

## Veiligheid

⚠️ **BELANGRIJK:**
- **Nooit** je token in GitHub zetten
- Gebruik `.gitignore` voor token bestanden
- Gebruikte environment variabelen in productie
- Roteer tokens regelmatig

### .gitignore voorbeeld:
```
*.token
.env
credentials.txt
access_token.txt
```

## Handige Links

- [Webex Developer Portal](https://developer.webex.com/)
- [Webex API Documentation](https://developer.webex.com/docs/api/basics)
- [Python Requests Library](https://docs.python-requests.org/)
- [REST API Basics](https://www.restapitutorial.com/)

## Geavanceerde Onderwerpen

### Webhooks
Luister naar Webex events met webhooks:
```python
# Zelf te implementeren
webhook_url = "https://jouw-server.com/webhook"
```

### Batch Operations
Voer meerdere operaties uit in één call

### Error Handling
```python
try:
    res = requests.get(url, headers=headers)
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## Lab 8.6.7 Informatie

Dit project is onderdeel van DevNet Associate training (Lab 8.6.7):
- Leer Webex Teams API basics
- Rooms en berichten beheren
- REST API principles toepassen
- Python HTTP requests gebruiken

## Resources Gebruikt

- **Requests library** - HTTP library voor Python
- **JSON** - Data format voor API communicatie
- **Webex Teams API v1** - Officiële Webex API
