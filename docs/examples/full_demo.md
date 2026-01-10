# Full Demo

This example demonstrates a complete end‑to‑end workflow using the Self‑Healing Localization Layer (SHL).  
It covers templates, language files, healing, UI integration, and runtime language switching.

---

# 1. Project Structure
```json
project/
├── main.py
└── locales/
├── template.json
├── en.json
└── fi.json
```

---

# 2. Template File (`template.json`)

```json
{
    "ui": {
        "title": "",
        "start_button": "",
        "exit_button": ""
    },
    "messages": {
        "welcome": "",
        "farewell": ""
    }
}
```
This defines the required structure for all languages.

---

# 3. Example Language Files

## en.json
```json
{
    "ui": {
        "title": "My Application",
        "start_button": "Start",
        "exit_button": "Exit"
    },
    "messages": {
        "welcome": "Welcome!",
        "farewell": "Goodbye!"
    }
}
```
## fi.json (intentionally incomplete)
```json
{
    "ui": {
        "title": "Sovellus"
    }
}
```
SHL will heal this automatically.

---

# 4. Main Program (main.py)
```python
from shl.engine import LocalizationEngine
```

# Initialize SHL
```python
engine = LocalizationEngine(base_language="en")
```

# Access localizers
```python
en = engine.localizer_for("en")
fi = engine.localizer_for("fi")
```

# UI class using SHL
```python
class MainMenuUI:
    def __init__(self, localizer):
        self.localizer = localizer
        self.refresh()

    def refresh(self):
        self.title = self.localizer.get("ui.title")
        self.start = self.localizer.get("ui.start_button")
        self.exit = self.localizer.get("ui.exit_button")
        self.welcome = self.localizer.get("messages.welcome")

    def render(self):
        print(f"\n=== {self.title} ===")
        print(f"[1] {self.start}")
        print(f"[2] {self.exit}")
        print(f"\n{self.welcome}")

# Create UI with English
ui = MainMenuUI(en)
ui.render()

# Switch to Finnish
print("\n--- Switching to Finnish ---")
ui.localizer = fi
ui.refresh()
ui.render()
```

---

# 5. Output Before Healing
If SHL did not heal files, Finnish output would be broken:
```
=== Sovellus ===
[1] ui.start_button
[2] ui.exit_button

messages.welcome
```
But SHL fixes this automatically.

---

# 6. Healed Finnish File (fi.json after SHL)
```json
{
    "ui": {
        "title": "Sovellus",
        "start_button": "",
        "exit_button": ""
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
* ensured structural consistency

---

# 7. Output After Healing
```
=== Sovellus ===
[1] 
[2] 
```
Even though translations are empty, the UI never crashes.

Developers can now fill in the missing Finnish translations safely.

---

# 8. Adding Missing Translations
## Update fi.json:
```json
{
    "ui": {
        "title": "Sovellus",
        "start_button": "Aloita",
        "exit_button": "Poistu"
    },
    "messages": {
        "welcome": "Tervetuloa!",
        "farewell": "Näkemiin!"
    }
}
```

---

# 9. Final Output
```
=== Sovellus ===
[1] Aloita
[2] Poistu

Tervetuloa!
```
---

# Summary
This full demo showed:
* how templates define structure
* how SHL loads and validates languages
* how missing keys are healed
* how UI components retrieve localized text
* how languages can be switched at runtime
* how SHL prevents missing‑key crashes
SHL provides a stable, predictable, and self‑maintaining localization system for any application.
