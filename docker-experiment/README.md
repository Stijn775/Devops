# Docker SQLite Experiment

Een simpel Docker container experiment met Flask en SQLite database.

## Wat doet het?

- Flask webserver met SQLite database
- Telt hoeveel keer je de pagina bezoekt
- Toont timestamp van elk bezoek
- Reset functie om database leeg te maken

## Hoe te gebruiken

### Stap 1: Bouw de Docker image
```bash
cd /home/devasc/labs/devnet-src/docker-experiment
docker build -t docker-experiment .
```

### Stap 2: Run de container
```bash
docker run -d -p 5000:5000 --name experiment-app docker-experiment
```

### Stap 3: Test de applicatie
Open in je browser:
- `http://localhost:5000` - Hoofdpagina (telt bezoeken)
- `http://localhost:5000/reset` - Reset de database

Of met curl:
```bash
curl http://localhost:5000
```

### Stap 4: Bekijk logs
```bash
docker logs experiment-app
```

### Stap 5: Stop en verwijder
```bash
docker stop experiment-app
docker rm experiment-app
```

## Docker Commando's

### Container beheren
```bash
# Status bekijken
docker ps

# Logs live volgen
docker logs -f experiment-app

# In de container gaan
docker exec -it experiment-app bash

# Database bestand bekijken
docker exec experiment-app ls -la experiment.db
```

### Image beheren
```bash
# Images bekijken
docker images

# Image verwijderen
docker rmi docker-experiment

# Image opnieuw bouwen
docker build -t docker-experiment . --no-cache
```

### Container opnieuw starten
```bash
docker restart experiment-app
```

## Uitbreidingen

### Met volume (data persistent)
```bash
docker run -d -p 5000:5000 \
  -v experiment-data:/app \
  --name experiment-app \
  docker-experiment
```

### Met andere poort
```bash
docker run -d -p 8080:5000 --name experiment-app docker-experiment
# Nu bereikbaar op http://localhost:8080
```

## Bestanden

- `app.py` - Flask applicatie met SQLite
- `Dockerfile` - Docker image configuratie
- `README.md` - Deze documentatie
