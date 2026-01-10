# AI Translation (Planned)

The `ai_translation` module is an optional extension for the Self‑Healing Localization Layer (SHL).  
It provides tools for generating draft translations using external AI providers.  
This module is designed to support workflows where large sets of localization keys need initial machine‑generated translations before human review.

> **Status:** Planned for version 0.2  
> This module is not yet included in the current release.

---

## Purpose

The goal of the AI translation module is to:

- accelerate the creation of new language files  
- reduce manual translation workload  
- provide consistent draft translations for human refinement  
- integrate seamlessly with SHL’s template‑driven workflow  

It is strictly optional — SHL remains fully functional without it.

---

## Planned Features

### **1. Automatic Translation via AI Providers**
Support for external translation engines such as:

- OpenAI  
- Azure AI  
- DeepL  
- Custom provider hooks  

The module will not bundle any provider by default.  
Instead, it will expose a clean interface for plugging in your own translation backend.

---

### **2. Batch Translation**
Translate entire language files or specific sections at once.

Example workflow:

- generate a new language file from the template  
- run batch translation to fill empty values  
- manually review and refine translations  

---

### **3. CLI Integration**
A command‑line interface is planned to support:

```bash
shl translate --lang fi --provider openai
```
This will allow automated translation as part of build scripts or localization pipelines.

```bash
from shl.ai_translation import AITranslator
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
translator = AITranslator(provider="openai", api_key="...")

translator.translate_missing_keys(engine, target_language="fi")
```

This example demonstrates:
* loading the engine
* initializing an AI translator
* filling missing keys in a target language

---

## Design Principles
The module follows SHL’s core philosophy:
* Non‑destructive  
Existing translations are never overwritten.
* Template‑aligned  
Only keys defined in `template.json` are translated.
* Provider‑agnostic  
Users choose their own AI provider.
* Opt‑in  
The module is not required for normal SHL operation.

---

## Roadmap
### Version 0.2
* Initial release
* Provider interface
* Batch translation
* CLI support

### Future Versions
* Translation memory
* Quality scoring
* Glossary enforcement
* Human‑in‑the‑loop review tools
  
---

## Summary
The ai_translation module extends SHL with optional AI‑powered translation capabilities.
It speeds up localization workflows while preserving SHL’s guarantees of safety, structure, and predictability.

This module is planned for version 0.2 and will evolve based on community feedback.
