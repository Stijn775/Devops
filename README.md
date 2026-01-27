# Git Instructies

## Repository Koppelen (eerste keer)
```bash
git remote add origin https://github.com/Stijn775/Devops.git
```

## Dagelijks Gebruik

### 1. Status Controleren
Bekijk welke bestanden zijn aangepast:
```bash
git status
```

### 2. Bestanden Toevoegen
Alle gewijzigde bestanden toevoegen:
```bash
git add .
```

Of specifieke bestanden:
```bash
git add bestandsnaam.txt
```

### 3. Wijzigingen Committen
```bash
git commit -m "Beschrijving van je wijzigingen"
```

### 4. Naar GitHub Pushen
```bash
git push
```

Of de eerste keer:
```bash
git push -u origin main
```

### 5. Wijzigingen Ophalen
Laatste versie van GitHub binnenhalen:
```bash
git pull
```

## Complete Workflow
Alles in één keer pushen naar GitHub:
```bash
git status
git add .
git commit -m "Jouw commit bericht"
git push
```

## Nuttige Commando's

### Repository Initialiseren (nieuwe repository)
```bash
git init
```

### Remote URL Controleren
```bash
git remote -v
```

### Commit Geschiedenis Bekijken
```bash
git log
```

### Laatste Wijzigingen Zien
```bash
git diff
```

### Branch Overzicht
```bash
git branch
```