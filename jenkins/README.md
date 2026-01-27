ea91e497fb8a42f5a2cb5e94a81602d6 <- admin password

## Jenkins Opstarten

### Stap 1: Jenkins Docker Container Starten
```bash
docker start jenkins_server
```

### Stap 2: Controleer of Jenkins draait
```bash
docker ps | grep jenkins
```

### Stap 3: Open Jenkins in browser
Ga naar: `http://localhost:8080`

Wacht 30-60 seconden tot Jenkins volledig is opgestart.

---

## Jenkins Job Aanmaken

### Stap 1: Inloggen
- Ga naar `http://localhost:8080`
- Username: `admin`
- Password: `ea91e497fb8a42f5a2cb5e94a81602d6`

### Stap 2: Nieuwe Job Aanmaken
1. Klik op **"New Item"** (linksboven)
2. Voer een naam in (bijv. `BuildAppJob`)
3. Selecteer **"Freestyle project"**
4. Klik op **"OK"**

### Stap 3: Source Code Management Configureren
1. Scroll naar **"Source Code Management"**
2. Selecteer **"Git"**
3. Vul bij **"Repository URL"** in: `https://github.com/Stijn775/Devops.git`
4. Bij **"Branches to build"** verander `*/master` naar `*/main`

### Stap 4: Build Step Toevoegen
1. Scroll naar **"Build Steps"**
2. Klik op **"Add build step"**
3. Selecteer **"Execute shell"**
4. Voer in het tekstvak in:
   ```bash
   bash ./jenkins/sample-app/sample-app.sh
   ```

### Stap 5: Opslaan en Bouwen
1. Klik onderaan op **"Save"**
2. Klik op **"Build Now"** (linksboven)
3. Bekijk de voortgang onder **"Build History"**
4. Klik op het build nummer en dan **"Console Output"** om logs te zien

---

## Jenkins Pipeline Aanmaken

### Stap 1: Nieuwe Pipeline Job
1. Klik op **"New Item"**
2. Voer een naam in (bijv. `SampleAppPipeline`)
3. Selecteer **"Pipeline"**
4. Klik op **"OK"**

### Stap 2: Pipeline Configureren
1. Scroll naar **"Pipeline"** sectie
2. Bij **"Definition"** selecteer **"Pipeline script from SCM"**
3. Bij **"SCM"** selecteer **"Git"**
4. Vul bij **"Repository URL"** in: `https://github.com/Stijn775/Devops.git`
5. Bij **"Branches to build"** vul in: `*/main`
6. Bij **"Script Path"** vul in: `Jenkinsfile` (dit bestand moet je nog aanmaken in je repo)

### Stap 3: Jenkinsfile Aanmaken (optioneel)
Als je een Jenkinsfile wilt gebruiken, maak dan een bestand `Jenkinsfile` aan in de root van je repository met bijvoorbeeld:

```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'bash ./jenkins/sample-app/sample-app.sh'
            }
        }
    }
}
```

### Stap 4: Pipeline Uitvoeren
1. Klik op **"Save"**
2. Klik op **"Build Now"**
3. Bekijk de stages en output

---

## Handige Commando's

### Jenkins stoppen
```bash
docker stop jenkins_server
```

### Jenkins logs bekijken
```bash
docker logs jenkins_server
```

### Jenkins herstart
```bash
docker restart jenkins_server
```