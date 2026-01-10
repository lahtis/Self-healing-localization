## Self‑Healing Localization ##
* A new paradigm for open‑source localization.
* This library eliminates missing translations forever by providing:
* Automatic creation of missing language files
* Automatic creation of missing keys
* Fallback to a base language
* Optional AI‑powered translation (with explicit user permission)
* Support for both UI text and AI prompt templates
* Never write localization files manually again.

'''
self-healing-localization/
│
├─ src/
│ ├─ shl/
│ │ ├─ __init__.py
│ │ ├─ localizer.py # Self-healing UI texts
│ │ ├─ template_localizer.py # Self-healing PromptEngine templates
│ │ ├─ engine.py # Connecting layer
│ │ └─ ai_translation.py # (optional) AI translations with permission
│
├─ examples/
│ ├─ basic_ui_localization.py
│ ├─ prompt_template_localization.py
│ └─ full_engine_demo.py
│
├─ tests/
│ ├─ test_localizer.py
│ ├─ test_template_localizer.py
│ └─ test_engine.py
│
├─ locales/
│ ├─ lang_en.json
│ └─ lang_fi.json
│
├─ prompts/
│ ├─ en.json
│ └─ fi.json
│
├─ README.md
├─ LICENSE
├─ pyproject.toml
└─ setup.cfg
'''
