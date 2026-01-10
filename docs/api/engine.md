# LocalizationEngine API

The `LocalizationEngine` is the central component of the Self‑Healing Localization Layer (SHL).  
It loads localization files, validates their structure, synchronizes languages, and provides access to translated text through the `Localizer` interface.

This document describes the public API of the engine.

---

## Class: LocalizationEngine

```python
class LocalizationEngine:
    def __init__(self, locales_path: str = "locales", base_language: str = "en"):
        ...
```

## Parameters
| Name          | Type | Default   | Description                                   |
|---------------|------|-----------|-----------------------------------------------|
| locales_path  | str  | "locales" | Directory containing all localization files.  |
| base_language | str  | "en"      | The primary language used for fallbacks.      |


---

## Attributes
### localizer
```python
engine.localizer
```
Returns an instance of `Localizer`, which provides access to translated strings using dot‑notation keys.

---

## Methods
### load()
```python
engine.load() -> None
```
Loads all localization files and the template from the locales/ directory.

## Responsibilities:
* read `template.json`
* read all `*.json` language files
* validate structure
* prepare internal caches
Called automatically during initialization.

---

### save()

```python
engine.save() -> None
```
Writes all in‑memory localization data back to disk.

Used after:
* healing missing keys
* generating new language files
* modifying translations programmatically

---

### heal()
```python
engine.heal() -> None
```
Runs the full self‑healing process:
* creates missing language files
* adds missing keys
* aligns structure with the template
* preserves existing translations
This method is called automatically during initialization, but can be triggered manually.

---

### get_languages()
```python
engine.get_languages() -> list[str]
```

Returns a list of available language codes, e.g.:
```python
["en", "fi", "sv"]
```

---

### get_template()
```python
engine.get_template() -> dict
```
Returns the parsed contents of `template.json`.

---

### get_language_data(language: str)
```python
engine.get_language_data("fi") -> dict
```
Returns the raw dictionary for a specific language.
Useful for tools, editors, or custom workflows.

---

## Usage Example
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine(locales_path="locales", base_language="en")

# Retrieve text
print(engine.localizer.get("menu.start"))

# Heal and save changes
engine.heal()
engine.save()
```
---

## Error Handling
The engine may raise:

## FileNotFoundError
If `template.json` is missing.

## ValueError
If a language file contains invalid `JSON`.

## KeyError
If a requested key does not exist and no fallback is available.

# Summary
The LocalizationEngine provides:
* automatic loading of localization files
* template‑driven validation
* full self‑healing behavior
* safe access to translations
* a clean API for integration
It is the recommended entry point for all SHL‑based applications.



