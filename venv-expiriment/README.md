# Virtual Environment Experiment

## Setup

### 1. Create Virtual Environment
```bash
python3 -m venv myenv
```

### 2. Activate Virtual Environment
```bash
# Linux/Mac
source myenv/bin/activate

# Windows
myenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Experiment

```bash
python3 experiment.py
```

## What Does It Do?

The `experiment.py` script demonstrates:
- ✓ Using virtual environments (venv)
- ✓ Installing packages with pip
- ✓ Making API calls with `requests` library
- ✓ Parsing JSON responses
- ✓ Error handling with try/except

## Deactivate Virtual Environment

```bash
deactivate
```

## Check Installed Packages

```bash
pip list
```

## Freeze Current Environment

```bash
pip freeze > requirements.txt
```

## Virtual Environment Structure

```
venv-expiriment/
├── myenv/              # Virtual environment directory
│   ├── bin/           # Executables (python, pip, activate)
│   ├── lib/           # Installed packages
│   └── pyvenv.cfg     # Configuration
├── experiment.py      # Your Python script
└── requirements.txt   # Package list
```
