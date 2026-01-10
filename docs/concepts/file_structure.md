# File Structure

The Self‑Healing Localization Layer (SHL) repository is organized into a clean and modular structure.  
This layout separates the core library, documentation, and examples, making the project easy to navigate and extend.

Below is the recommended directory layout for projects using SHL.

```
Self-healing-localization/
├── shl/
│   ├── init.py
│   ├── engine.py
│   ├── localizer.py
│   ├── template_localizer.py
│   └── ai_translation.py
│
├── docs/
│   ├── index.md
│   ├── installation.md
│   ├── concepts/
│   ├── guides/
│   ├── api/
│   └── examples/
│
├── examples/
│   ├── basic_usage/
│   └── (more examples coming)
│
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## **shl/** — Core Library

This directory contains the actual Python package.

### `engine.py`
The main orchestrator responsible for:
- loading localization files  
- validating structure  
- synchronizing languages  
- managing the self‑healing process  

### `localizer.py`
Provides the API for retrieving localized strings using dot‑notation keys.

### `template_localizer.py`
Handles template generation and synchronization.

### `ai_translation.py`
Optional helper module for AI‑assisted translation workflows.

---

## **docs/** — Project Documentation

Contains all documentation pages, organized into logical sections:

- **index.md** — documentation homepage  
- **installation.md** — installation instructions  
- **concepts/** — architectural and conceptual explanations  
- **guides/** — step‑by‑step tutorials  
- **api/** — API reference for each module  
- **examples/** — documentation‑side examples  

This folder will grow as the project evolves.

---

## **examples/** — Code Examples

Contains runnable examples demonstrating:

- basic usage of the engine  
- how to structure localization files  
- how to integrate SHLL into real projects  

More examples will be added over time.

---

## Root Files

### `pyproject.toml`
Modern build configuration for packaging and distribution.

### `README.md`
Overview of the project, installation, and quickstart instructions.

### `LICENSE`
Open‑source license for the project.

---

## Summary

The SHLL repository is structured to be:

- **clear** — easy to navigate  
- **modular** — core code, docs, and examples separated  
- **extensible** — ready for future features and documentation  
- **maintainable** — clean boundaries between components  

This structure supports both contributors and users, ensuring long‑term project health.

---

