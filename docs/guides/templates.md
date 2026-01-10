# Templates

Templates define the canonical structure for all localization files in SHL.  
They ensure that every language follows the same schema, enabling SHL’s self‑healing behavior.

This guide explains how templates work, how to modify them, and how SHL uses them to maintain consistency across all languages.

---

# 1. What Is a Template?

A template is a JSON file named `template.json` located in the `locales/` directory.

It defines:

- the required keys  
- the required nesting structure  
- the shape of all language files  
- empty values (placeholders for translations)

Example:

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
This structure becomes the “source of truth” for all languages.

---

# 2. How SHL Uses Templates
SHL loads the template at startup and uses it to:
* generate new language files
* validate existing languages
* add missing keys
* restore missing sections
* ensure structural consistency
Templates are the backbone of SHL’s self‑healing system.

---

# 3. Modifying the Template
When you add new keys or sections to template.json, SHL will automatically propagate these changes to all languages.

Example: Adding a new key
```json
{
    "messages": {
        "welcome": "",
        "farewell": "",
        "error": ""
    }
}
```

After modifying the template, run:
```python
engine.sync()
```
SHL will:
* add messages.error to every language
* preserve existing translations
* never overwrite human‑written text

---

# 4. Creating New Languages from the Template
To create a new language:
```python
engine.ensure_language("de")
```


