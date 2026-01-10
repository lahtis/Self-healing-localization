# Localization Engine

The `LocalizationEngine` is the central orchestrator of the Self‑Healing Localization Layer (SHL).  
It is responsible for loading localization data, validating structure, synchronizing languages, and enabling the system’s self‑healing behavior.

The engine is the recommended entry point for all applications using SHL.

---

## Core Responsibilities

The `LocalizationEngine` handles the following tasks:

- **Loading languages**  
  Reads all JSON language files from the `locales/` directory.

- **Retrieving localized text**  
  Provides access to translated strings through the `Localizer` interface.

- **Managing templates**  
  Loads and maintains the base `template.json` file that defines the canonical structure for all languages.

- **Synchronizing languages**  
  Ensures that every language file matches the structure of the template.

- **Self‑healing behavior**  
  Automatically adds missing keys, creates missing language files, and keeps the entire localization set consistent.

---

## Localization Directory locales/

This directory must contain:

- **One JSON file per language**  
  Examples:  
  - `en.json`  
  - `fi.json`  
  - `sv.json`

- **A base template file**  
  `template.json` defines the required structure for all languages.

---

## Example Language File (`en.json`)

```json
{
    "menu": {
        "start": "Start",
        "exit": "Exit"
    },
    "errors": {
        "network": "Network error occurred."
    }
}
```

## Example Template File (template.json)
```json
{
    "menu": {
        "start": "",
        "exit": ""
    },
    "errors": {
        "network": ""
    }
}
```
The template defines the required keys but leaves values empty.
The engine uses this file to validate and synchronize all languages.

# Self‑Healing Behavior
The LocalizationEngine ensures that:

## 1. Missing language files are created
If locales/fi.json does not exist, it is automatically generated from template.json.

## 2. Missing keys are added
If a language file lacks a key present in the template, the engine inserts it with an empty value.

## 3. Structural mismatches are corrected
Nested objects, missing sections, or outdated structures are aligned with the template.

## 4. No existing translations are overwritten
Self‑healing only adds missing data — it never replaces existing text.

## Integration Flow
A typical application uses the engine like this:
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine()

# Retrieve localized text
text = engine.localizer.get("menu.start")
print(text)
```
The engine handles all loading, validation, and synchronization automatically.

## Summary
The LocalizationEngine is the backbone of SHL.
It provides:
* predictable behavior
* automatic synchronization
* safe and non-destructive updates
* a clean API for retrieving localized text

This module ensures that localization remains consistent, maintainable, and scalable as your project grows.
