# Self‑Healing Localization

Self‑healing is the core feature that defines the Self‑Healing Localization Layer (SHL).  
It ensures that all localization files remain complete, consistent, and structurally aligned with the base template — automatically and safely.

SHL does not overwrite existing translations.  
It only fills in what is missing.

---

## What “Self‑Healing” Means

SHL continuously validates and synchronizes all language files against the base template (`template.json`).  
Whenever inconsistencies are found, SHL repairs them automatically.

The system guarantees that:

### **1. Missing language files are created**
If a language file does not exist (e.g., `locales/fi.json`), SHL generates it from the template.

### **2. Missing keys are added**
If a language file lacks keys that exist in the template, SHL inserts them with empty values:

```json
"menu": {
    "start": "Start",
    "exit": ""
}
```

### 3. Structural mismatches are corrected
If the structure of a language file diverges from the template (missing sections, wrong nesting, outdated layout), SHL realigns it automatically.

### 4. Existing translations are preserved
SHL never overwrites user‑provided translations.
Only missing or invalid parts are repaired.

### 5. Fallback behavior is guaranteed
If a translation is missing, SHL ensures a safe fallback to the base language.

---

### Why Self‑Healing Matters
Traditional localization systems often break when:
* a new key is added
* a section is renamed
* a language file is missing
* translators forget to update a file
* the structure drifts over time

SHL eliminates these problems by enforcing a single source of truth (`template.json`) and keeping all languages synchronized with it.

This results in:
* fewer runtime errors
* no “missing translation” crashes
* predictable behavior
* easier maintenance
* safer refactoring

### Example: Before and After Healing
Before

```json
{
    "menu": {
        "start": "Start"
    }
}
```
Template:
```json
{
    "menu": {
        "start": "",
        "exit": ""
    }
}
```
## After SHL Healing
`en.json` becomes:
```json
{
    "menu": {
        "start": "Start",
        "exit": ""
    }
}
```
The missing key is added, but the existing translation is preserved.

---

## Summary
Self‑healing is the foundation of SHL.
It ensures that:
* all languages stay complete
* all structures stay synchronized
* no translations are lost
* no missing keys cause errors
* localization remains stable as your project grows

This makes SHL a reliable, low‑maintenance solution for any application that needs clean, predictable localization.
