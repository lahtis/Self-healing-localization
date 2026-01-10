# Example: Synchronizing Languages

The `sync()` operation ensures that all localization files match the structure defined in `template.json`.  
It is a high‑level shortcut for running SHL’s full self‑healing process across every language.

This example demonstrates how to use `engine.sync()` and what happens before and after synchronization.

---

# 1. Before Synchronization

Assume the following project structure:
```json
locales/
├── template.json
├── en.json
└── fi.json
```

## Template (`template.json`)

```json
{
    "menu": {
        "start": "",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "farewell": ""
    }
}
```
## Incomplete Finnish File (`fi.json`)

```json
{
    "menu": {
        "start": "Aloita"
    }
}
```
## #The Finnish file is missing:
* menu.exit
* messages.welcome
* messages.farewell

---

# 2. Running Synchronization
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
engine.sync()
```
`sync()` performs:
* loading all languages
* comparing each file to the template
* adding missing keys
* restoring missing sections
* preserving existing translations
* writing healed files back to disk

It is equivalent to:

```python
engine.heal()
engine.save()
```

---

# 3. After Synchronization
The healed `fi.json` becomes:
```json
{
    "menu": {
        "start": "Aloita",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "farewell": ""
    }
}
```
SHL:
* kept the existing translation (`Aloita`)
* added missing keys
* restored missing sections
* ensured full structural alignment

---

# 4. Using Synchronized Data
After synchronization, your UI or application can safely retrieve any key:
```python
localizer = engine.localizer_for("fi")

print(localizer.get("menu.start"))     # Aloita
print(localizer.get("menu.exit"))      # ""
print(localizer.get("messages.welcome"))  # ""
```

* No missing‑key errors.
* No crashes.
* Predictable behavior.

  ---

# 5. When to Use sync()
Use `engine.sync()` when:
* adding new keys to the template
* adding new sections
* adding a new language
* preparing a release build
* validating localization before deployment
It ensures all languages are complete and consistent.
  
  ---

# Summary
`engine.sync()` is the easiest way to keep all localization files aligned with the template.
It runs SHL’s full self‑healing process and guarantees that every language file is structurally correct and safe to use.

This makes localization predictable, stable, and maintenance‑free.
  
