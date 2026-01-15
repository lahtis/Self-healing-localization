"""
File: language_manager.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
SHL’s language engine: loads and saves localization files,
returns texts, and auto‑creates missing keys through self‑healing.

SHL:n kielimoottori: lataa ja tallentaa lokalisointitiedostot, 
palauttaa tekstit ja luo puuttuvat avaimet automaattisesti.”
"""
import json
import os

class LanguageManager:
    def __init__(self, lang_code="fi", locales_path="locales"):
        self.lang_code = lang_code
        self.locales_path = locales_path
        self.lang_file = os.path.join(locales_path, f"lang_{lang_code}.json")

        # Ensure locales directory exists
        if not os.path.exists(locales_path):
            os.makedirs(locales_path)

        # Load or create language file
        self.texts = self._load_language_file()

    # -------------------------
    # Internal helpers
    # -------------------------
    def _load_language_file(self):
        if not os.path.exists(self.lang_file):
            return {}

        try:
            with open(self.lang_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}

    def _save_language_file(self):
        with open(self.lang_file, "w", encoding="utf-8") as f:
            json.dump(self.texts, f, indent=4, ensure_ascii=False)

    # -------------------------
    # Public API
    # -------------------------
    def get_text(self, key, default=""):
        """
        Returns the localized text for a given key.
        If the key does not exist, it is automatically created (self-healing).
        """
        if key not in self.texts:
            self.texts[key] = default
            self._save_language_file()

        return self.texts.get(key, default)

    def get_component_texts(self, component):
        """
        Given an SHLComponent instance, returns a dict of all its text fields.
        Example:
            {
                "label": "Save",
                "placeholder": "Enter name..."
            }
        """
        result = {}
        for field_name, key in component.text_keys.items():
            result[field_name] = self.get_text(key, default=field_name)
        return result

    def set_language(self, lang_code):
        """
        Switches the active language and reloads the file.
        """
        self.lang_code = lang_code
        self.lang_file = os.path.join(self.locales_path, f"lang_{lang_code}.json")
        self.texts = self._load_language_file()

    def __repr__(self):
        return f"<LanguageManager lang='{self.lang_code}'>"

