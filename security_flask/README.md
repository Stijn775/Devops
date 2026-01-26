# Security Flask - Password Evolution Lab

Dit project demonstreert twee password security methodes:
- **v1** - Plain text passwords (ONVEILIG ⚠️)
- **v2** - Hashed passwords (VEILIGER ✓)

## Server Starten

```bash
python3 password-evolution.py
# Server draait op https://localhost:5000 (self-signed SSL)

# Of achtergrond
nohup python3 password-evolution.py &

# Server stoppen
pkill -f password-evolution.py
```

## API Methodes

### 1. `index()` - GET /

Welkomstpagina

```bash
curl https://localhost:5000 -k
```

Response: `Welcome to the hands-on lab for an evolution of password systems!`

---

### 2. `signup_v1()` - POST /signup/v1

**Plain text wachtwoord opslaan** (ONVEILIG!)

Slaat username + password direct (ongehasht) op in SQLite tabel `USER_PLAIN`

```bash
curl -X POST https://localhost:5000/signup/v1 \
  -d "username=alice" \
  -d "password=secret123" -k
```

Response: `signup success`

---

### 3. `verify_plain()` - Helper function

Verifies plain text password door direct te vergelijken met database waarde

---

### 4. `login_v1()` - POST /login/v1

**Plain text verificatie** 

Verifieert username + password tegen plaintext waarden in database

```bash
curl -X POST https://localhost:5000/login/v1 \
  -d "username=alice" \
  -d "password=secret123" -k
```

Response: `login success`

---

### 5. `signup_v2()` - POST /signup/v2

**SHA256 hashed wachtwoord opslaan** (VEILIGER!)

Hasht password met SHA256 en slaat hash op in tabel `USER_HASH`

```bash
curl -X POST https://localhost:5000/signup/v2 \
  -d "username=bob" \
  -d "password=mypass" -k
```

Response: `signup success`

---

### 6. `verify_hash()` - Helper function

Verifies hashed password door hash van inkomend password te vergelijken met opgeslagen hash

---

### 7. `login_v2()` - POST /login/v2

**SHA256 hash verificatie**

Verifieert username + password door hashes te vergelijken

```bash
curl -X POST https://localhost:5000/login/v2 \
  -d "username=bob" \
  -d "password=mypass" -k
```

Response: `login success`

---

## Database Inspectie

```bash
sqlite3 test.db

# V1 tabel (plaintext!)
SELECT * FROM USER_PLAIN;

# V2 tabel (hashes)
SELECT * FROM USER_HASH;

.quit
```

---

## Security Vergelijking

| Aspect | v1 | v2 |
|--------|-----|-----|
| **Opslag** | Plain text | SHA256 hash |
| **Database lek** | ❌ Passwords exposed | ✓ Hashes only |
| **Veilig** | ❌ NEEN | ✓ JA |

---

## Volledig Test Scenario

```bash
# 1. Start server
python3 password-evolution.py

# 2. Signup v1
curl -X POST https://localhost:5000/signup/v1 -d "username=user1" -d "password=pass1" -k

# 3. Login v1
curl -X POST https://localhost:5000/login/v1 -d "username=user1" -d "password=pass1" -k

# 4. Signup v2
curl -X POST https://localhost:5000/signup/v2 -d "username=user2" -d "password=pass2" -k

# 5. Login v2
curl -X POST https://localhost:5000/login/v2 -d "username=user2" -d "password=pass2" -k

# 6. Check database
sqlite3 test.db "SELECT * FROM USER_PLAIN; SELECT * FROM USER_HASH;"

# 7. Stop server
pkill -f password-evolution.py
```
