# Sample Flask App

Simple Flask web application dat toont welk IP adres jou belt.

## Wat doet het?

GET `/` endpoint retourneert: `You are calling me from [IP_ADDRESS]`

## Lokaal Runnen

```bash
# Direct met Python
python3 sample_app.py
# Server draait op http://localhost:8080

# Test in ander terminal
curl http://localhost:8080
```

## Docker Runnen

### Automatisch met script

```bash
bash sample-app.sh
```

Dit script:
1. Maakt tempdir aan met Dockerfile
2. Bouwt Docker image (`sampleapp`)
3. Draait container op port 8080
4. Toont actieve containers

### Handmatig met Docker

```bash
# Build image
docker build -t sampleapp .

# Run container
docker run -t -d -p 8080:8080 --name samplerunning sampleapp

# Test
curl http://localhost:8080

# Logs zien
docker logs samplerunning

# Running Containers Bekijken
docker ps -a

# Stop
docker stop samplerunning
docker stop "eerste 4 getallen"

# Remove
docker rm samplerunning
docker rm "eerste 4 getallen"
```

## Vereisten

- Python 3.8+
- Flask 3.0+
- Docker (voor Docker variant)

## Files

- `sample_app.py` - Flask application
- `sample-app.sh` - Docker build + run script
- `static/` - CSS files
- `templates/` - HTML templates
