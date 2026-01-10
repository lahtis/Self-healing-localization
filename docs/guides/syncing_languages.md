# Synchronizing Languages

SHL provides a simple way to ensure that all localization files stay aligned with the structure defined in `template.json`.  
The `sync()` method runs the full self‑healing process across every language and writes the updated files back to disk.

This guide explains how synchronization works, when to use it, and what happens internally.

---

# 1. What Does Synchronization Do?

Calling:

```python
engine.sync()
```

performs the following steps:
* 1. Loads the template (template.json)
* 2. Loads all language files in locales/
* 3. Compares each language file to the template
* 4. Adds missing keys
* 5. Restores missing sections
* 6. Preserves existing translations
* 7. Writes healed files back to disk
Synchronization never overwrites existing translations.

---

# 2. Before Synchronization
Assume the following structure:
```python
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
## Incomplete Finnish File (fi.json)
```json
{
    "menu": {
        "start": "Aloita"
    }
}
```
The Finnish file is missing:

* `menu.exit`
* `messages.welcome`
* `messages.farewell`

---

# 3. Running Synchronization
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
engine.sync()
```

This is equivalent to:
```python
engine.heal()
engine.save()
```

---

# 4. After Synchronization
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
* preserved existing translations
* added missing keys
* restored missing sections
* ensured full structural alignment

---

# 5. Using Synchronized Languages
After synchronization, your application can safely access any key:
```python
localizer = engine.localizer_for("fi")

print(localizer.get("menu.start"))       # Aloita
print(localizer.get("menu.exit"))        # ""
print(localizer.get("messages.welcome")) # ""
```
* No missing‑key errors.
* No crashes.
* Predictable behavior.

---

# 6. When Should You Use sync()?
Use synchronization when:
* adding new keys to the template
* adding new sections
* adding a new language
* preparing a release build
* validating localization before deployment
* integrating SHL into CI/CD pipelines
It ensures all languages are complete and consistent.

---

7. How sync() Differs From Other Methods

| Method             | Purpose                                           |
|--------------------|---------------------------------------------------|
| `ensure_language()` | Creates a new language file or heals a single language. |
| `heal()`            | Heals all languages in memory but does not save. |
| `save()`            | Writes in‑memory data to disk.                   |
| `sync()`            | Full heal + save for all languages.              |


`sync()` is the highest‑level operation.

---

# Summary
`engine.sync()` is the easiest and safest way to keep all localization files aligned with the template.
It runs SHL’s full self‑healing process and guarantees that every language file is structurally correct and ready for use.

This makes localization predictable, stable, and maintenance‑free.

---
