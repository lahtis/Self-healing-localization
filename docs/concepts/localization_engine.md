# Localization Engine

The `LocalizationEngine` is the high‑level interface that:

- loads languages  
- retrieves UI text  
- retrieves templates  
- synchronizes all languages  
- ensures self‑healing behavior  

It is the recommended entry point for all applications.

## Localization Directory

All translation files are stored inside the `locales/` directory.  
SHLL expects this directory to contain:

- **One JSON file per language**  
  Example: `en.json`, `fi.json`, `sv.json`

- **A base template file**  
  `template.json` defines the canonical structure for all languages.

### Example language file (`en.json`)

```json
{
    "menu": {
        "start": "Start",
        "exit": "Exit"
    },
    "errors": {
        "network": "Network error occurred."
    }
}



SHLL uses two directories:

locales/
lang_en.json
lang_fi.json
...

prompts/
en.json
fi.json
...

The engine ensures these files exist and remain synchronized.


