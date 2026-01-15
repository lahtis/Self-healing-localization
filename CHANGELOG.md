# Changelog
All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.2.0] — Unreleased
> This version is available in the GitHub repository but has not yet been published to PyPI.

### Added
- New modular project structure with clear layer separation:
  - core, registry, middleman, healer, adapters, ui_tree, diff, utils
- UI Tree system:
  - UINode model
  - UITreeBuilder interface
  - UITreePrinter debugging tool
- UI Schema v1 (schema/v1) with component definitions
- UI Components directory with component metadata and structure
- Comprehensive documentation across the project:
  - README for ui_tree, utils, schema/v1, components
  - Core Concepts (What SHL is, diff vs patch vs heal, scoring model)
  - Future extension roadmaps for multiple directories
- Initial utils directory for shared helper modules
- Project‑wide architectural descriptions and onboarding improvements

### Changed
- Reorganized repository layout for clarity and scalability
- Updated documentation to reflect new architecture
- Improved naming conventions and directory hierarchy
- Clarified healer, diff and patch terminology and responsibilities

### Removed
- Legacy localization‑only structure from the original 0.1.0 release
- Old engine‑based architecture in favor of layered model

### Notes
This version represents a major architectural evolution of SHL.
The system now focuses on a deterministic, layered self‑healing model
instead of the earlier file‑based localization engine.

---

## [0.1.1] - 2026-01-10
### Added
- Initial release of the **Self‑Healing Localization Layer (SHLL)**.
- `localizer.py`:  
  - Automatic creation of missing UI language files.  
  - Automatic creation of missing UI keys.  
  - Fallback to base language (`en`).  
  - Self‑healing behavior for all UI text lookups.

- `template_localizer.py`:  
  - Automatic creation of missing prompt template language files.  
  - Automatic copying of base template (`en.json`) when a language is missing.  
  - Automatic creation of missing template keys.  
  - Self‑healing behavior for all template lookups.

- `engine.py`:  
  - Unified high‑level interface for UI and template localization.  
  - `ensure_language()` for creating all required files for a new language.  
  - `sync()` for synchronizing all languages with the base language.  
  - Clean API for retrieving UI text and templates.

### Notes
- This version focuses on core functionality and stability.  
- AI‑powered translation is planned for **v0.3**.  
- CLI tooling and Localization Studio are planned for future releases.

### [Unreleased]
#### Planned
- AI‑powered translation module (Gemini / Groq / OpenAI).  
- CLI tool (`selfheal sync`, `selfheal translate`).  
- Automatic detection of missing keys across all languages.  
- Web‑based Localization Studio.  
- Visual diffing of translations.  
- Export/import of language packs.  
- Framework integrations (Flask, FastAPI, Django, Flet).  

---

## [0.1.0] — Initial Release
- The initial release version. The structure existed, but the system was still clearly incomplete and partially broken.
  
---
