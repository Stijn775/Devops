# Unit Testing - Recursive JSON Search Project

## Overzicht
Dit project demonstreert unit testing in Python met de `unittest` framework. Het bevat een recursieve JSON search functie die keys zoekt in geneste JSON objecten, met bijbehorende tests.

## Doel
- Leer hoe je een recursieve functie schrijft voor JSON parsing
- Begrijp unit testing met `unittest`
- Schrijf test cases voor verschillende scenario's
- Test functies met nested dictionaries en lists

## Bestandbeschrijving

### Core Bestanden

| Bestand | Beschrijving |
|---------|-------------|
| `recursive_json_search.py` | Functie die recursief keys in JSON zoekt |
| `test_data.py` | Test data - JSON sample data en test keys |
| `test_json_search.py` | Unit tests voor de search functie |

## Functie Uitleg

### `json_search(key, input_object)`

Zoekt een gegeven key in een genest JSON object/dictionary.

**Parameters:**
- `key` (str) - Key naam om te zoeken (case sensitive)
- `input_object` (dict/list) - JSON object of list om te doorzoeken

**Return:**
- List van dictionaries met gevonden key:value pairs
- Lege list als key niet gevonden is

**Hoe het werkt:**
1. Controleert of input een dictionary is
2. Zoekt de gegeven key in het dictionary
3. Als gevonden, voegt het toe aan resultaat
4. Voor nested dictionaries/lists: recursief doorzoeken
5. Geeft alle gevonden matches terug

**Voorbeeld:**
```python
from recursive_json_search import json_search
from test_data import data, key1

result = json_search("issueSummary", data)
print(result)  # [{'issueSummary': 'Device unreachable'}]
```

## Test Data

### `test_data.py` bevat:

| Variabele | Waarde | Beschrijving |
|-----------|--------|-------------|
| `key1` | "issueSummary" | Key die WEL in data zit |
| `key2` | "XY&^$#*@!1234%^&" | Key die NIET in data zit |
| `data` | Complex JSON object | Genest JSON met arrays en dicts |

De test data bevat:
- Top-level keys
- Nested dictionaries
- Lists met objecten
- Meerdere niveaus van nesting

## Unit Tests

### `test_json_search.py` bevat 3 tests:

#### 1. `test_search_found()`
```python
def test_search_found(self):
    '''key should be found, return list should not be empty'''
    self.assertTrue([]!=json_search(key1,data))
```
- **Test:** Zoekt naar `key1` die WEL in data zit
- **Verwacht:** List is niet leeg (gevonden!)
- **Assertion:** `assertTrue([] != result)`

#### 2. `test_search_not_found()`
```python
def test_search_not_found(self):
    '''key should not be found, should return an empty list'''
    self.assertTrue([]==json_search(key2,data))
```
- **Test:** Zoekt naar `key2` die NIET in data zit
- **Verwacht:** Lege list (niet gevonden)
- **Assertion:** `assertTrue([] == result)`

#### 3. `test_is_a_list()`
```python
def test_is_a_list(self):
    '''Should return a list'''
    self.assertIsInstance(json_search(key1,data),list)
```
- **Test:** Check of return waarde een list is
- **Verwacht:** Return type is `list`
- **Assertion:** `assertIsInstance(result, list)`

## Unittest Framework

### Basis Structuur

```python
import unittest

class MyTestClass(unittest.TestCase):
    def test_something(self):
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
```

### Veelgebruikte Assertions

| Assertion | Doel |
|-----------|------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x is True |
| `assertFalse(x)` | x is False |
| `assertIsNone(x)` | x is None |
| `assertIsNotNone(x)` | x is not None |
| `assertIsInstance(a, b)` | isinstance(a, b) |
| `assertIn(a, b)` | a in b |
| `assertNotIn(a, b)` | a not in b |
| `assertRaises(Exception)` | Exception wordt geraised |

## Hoe Te Gebruiken

### 1. Run Alle Tests
```bash
python3 -m unittest
```

### 2. Run Specifieke Test Module
```bash
python3 -m unittest test_json_search
```

### 3. Run Specifieke Test Class
```bash
python3 -m unittest test_json_search.json_search_test
```

### 4. Run Specifieke Test Method
```bash
python3 -m unittest test_json_search.json_search_test.test_search_found
```

### 5. Verbose Output
```bash
python3 -m unittest -v
```

### 6. Direct Script Draaien
```bash
python3 recursive_json_search.py
python3 test_json_search.py
```

## Output Voorbeelden

### Succesvolle Tests
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

### Mislukte Test
```
F
----------------------------------------------------------------------
FAIL: test_search_found (test_json_search.json_search_test)
key should be found, return list should not be empty
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_json_search.py", line 8, in test_search_found
    self.assertTrue([]!=json_search(key1,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

## Recursie Uitleg

De `json_search` functie gebruikt recursie:

```
json_search("issueSummary", data)
├── Check if dict? YES
├── Loop through keys
│   ├── Found "issueSummary"? YES → Add to list
│   ├── Check nested dict? YES → Recursive call
│   └── Check list items? YES → Check each item
│       ├── Is item dict/list? YES → Recursive call
│       └── Is item dict/list? NO → Skip
└── Return list of all matches
```

## Voordelen van Recursie Hier

1. **Geneste Structures** - Handelt willekeurig diep nesting af
2. **Flexibel** - Werkt met dicts, lists en mixed structures
3. **Schoon Code** - Less code dan nested loops
4. **Herbruikbaar** - Dezelfde logica voor alle niveaus

## Best Practices voor Testing

1. **Test Naming** - `test_` prefix voor alle test methods
2. **Descriptive Names** - `test_search_found` niet `test_1`
3. **Docstrings** - Uitleg wat elke test doet
4. **One Assertion Per Test** - Test één ding per method
5. **Setup/Teardown** - Gebruik `setUp()` voor shared test data

## Geavanceerde Voorbeelden

### Eigen Test Cases Toevoegen

```python
def test_empty_dict(self):
    '''Test with empty dictionary'''
    result = json_search("key", {})
    self.assertEqual(result, [])

def test_empty_list(self):
    '''Test with empty list'''
    result = json_search("key", [])
    self.assertEqual(result, [])

def test_multiple_matches(self):
    '''Test when key appears multiple times'''
    test_data = {
        "name": "value1",
        "nested": {"name": "value2"}
    }
    result = json_search("name", test_data)
    self.assertEqual(len(result), 2)
```

### Test Discovery Pattern

```bash
# Run tests matching pattern
python3 -m unittest discover -p "test_*.py"

# Verbose with patterns
python3 -m unittest discover -p "test_*.py" -v
```

## Troubleshooting

### Tests Runnen Niet
```bash
# Check syntax errors
python3 -m py_compile test_json_search.py

# Check imports
python3 -c "from test_json_search import *"
```

### AssertionError
- Check expected vs actual waarden
- Print debug info in test
- Verhoog verbosity: `-v` flag

### Import Errors
- Zorg `.py` files in dezelfde directory staan
- Check `__init__.py` exists (als packages)
- Verify imports in bestanden

## Lab Informatie

Dit project is onderdeel van DevNet Associate training:
- **Lab:** Unit Testing Basics
- **Onderwerp:** Python Testing Framework
- **Doelen:**
  - Begrijp recursie
  - Leer unittest framework
  - Schrijf goede test cases
  - Test driven development basics

## Handige Links

- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Testing Best Practices](https://docs.pytest.org/en/latest/getting-started.html)
- [Recursion Explained](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)
- [JSON in Python](https://docs.python.org/3/library/json.html)

## Volgende Stappen

1. Voeg meer test cases toe
2. Test edge cases (empty inputs, single items, etc)
3. Leer pytest als alternatief voor unittest
4. Implementeer test coverage reporting
5. Setup continuous testing (CI/CD)
