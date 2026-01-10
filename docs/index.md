# Self‑Healing Localization Layer (SHLL)

Welcome to the official documentation for the **Self‑Healing Localization Layer**, a lightweight and dependency‑free localization system for Python applications.

SHLL is designed to eliminate common localization problems by automatically:

- creating missing language files
- adding missing translation keys
- synchronizing all languages with a shared base template
- preventing translation drift as your project grows

This makes SHLL ideal for games, tools, and applications where clarity, maintainability, and long‑term consistency matter.

---

## Key Features

- **Self‑healing architecture**  
  Automatically detects missing or outdated keys and updates language templates without overwriting existing translations.

- **Minimalistic and predictable design**  
  Built with a Nordic mindset: clean structure, no unnecessary dependencies, and long‑term maintainability.

- **Template‑driven workflow**  
  Ensures all languages follow the same schema, reducing errors and manual work.

- **Developer‑friendly API**  
  Simple interfaces for loading, retrieving, and managing localized strings.

---

## Documentation Structure

This documentation includes:

- **Installation**  
  How to install SHLL from TestPyPI or PyPI.

- **Concepts**  
  Core ideas behind the architecture and design philosophy.

- **Guides**  
  Step‑by‑step instructions for integrating SHLL into your project.

- **API Reference**  
  Detailed documentation for `LocalizationEngine`, `Localizer`, `TemplateLocalizer`, and other modules.

- **Examples**  
  Practical usage examples and recommended project structures.

- **Roadmap**  
  Planned features and future development directions.

---

## Getting Started

To install the latest version:

```bash
pip install self-healing-localization
```

Basic usage:
```bash
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
text = engine.localizer.get("menu.start")
print(text)
```

## About the Project
SHLL is an open‑source project focused on clarity, maintainability, and developer empowerment.
Feedback, ideas, and contributions are warmly welcome.

Repository:
https://github.com/lahtis/Self-healing-localization


