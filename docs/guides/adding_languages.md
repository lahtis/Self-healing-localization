# Adding New Languages

SHL makes it easy to add new languages to your project.  
The system automatically generates all required files and ensures they follow the structure defined in `template.json`.

This guide explains how to create a new language and how SHL keeps it synchronized.

---

# 1. Creating a New Language

To add a new language, call:

```python
engine.ensure_language("de")
```
This will automatically create:

* `locales/lang_de.json`
* `prompts/de.json` (if prompt templates are used)
Both files are generated using the structure from `template.json`.

---

# 2. Generated Language File
A new language file contains all required keys but empty values:
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
This ensures translators always start with a complete and correct structure.

---

# 3. Healing Existing Languages
If the language already exists, SHL will:
* add missing keys
* restore missing sections
* preserve existing translations
* ensure structural consistency

## Example:
### Before (`lang_de.json`)
```json
{
    "menu": {
        "start": "Starten"
    }
}
```
### After ensure_language("de")
```json
{
    "menu": {
        "start": "Starten",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "farewell": ""
    }
}
```

---

# 4. Using the New Language
Once created, you can access it through the engine:
```python
de_localizer = engine.localizer_for("de")
print(de_localizer.get("menu.start"))
```
Or switch UI language dynamically:
```python
ui.localizer = engine.localizer_for("de")
ui.refresh()
```

---

# 5. When to Use ensure_language()
Use this method when:
* adding a new language to your project
* preparing a translation workflow
* integrating SHL into a multilingual application
* validating that all languages exist before deployment
It guarantees that every language is complete and ready for translation.

---

# Summary
Adding a new language in SHL is simple and safe:
* one function call
* automatic file generation
* full template alignment
* no missing keys
* no risk of overwriting existing translations
SHL ensures your localization system stays predictable and easy to maintain as your project grows.
