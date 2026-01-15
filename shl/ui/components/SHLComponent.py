"""
File: SHLComponent.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
SHL component model: loads the UI schema, locates the component definition, and exposes a unified interface 
for text keys, framework‑specific implementations, and metadata. Serves as the fundamental UI unit connecting 
schema, adapters, and middleman logic

SHL‑komponenttimalli: lataa UI‑skeeman, etsii komponentin määritelmän ja tarjoaa yhtenäisen rajapinnan komponentin
tekstikentille, framework‑kohtaisille toteutuksille ja metatiedoille. Toimii UI‑kerroksen perusyksikkönä ja 
yhdistää skeeman, adapterit ja middleman‑logiikan.
"""
import json
import os

class SHLComponent:
    def __init__(self, component_id, schema_path="shl/ui/schema/v1/ui_schema.json"):
        self.component_id = component_id
        self.schema_path = schema_path
        self.schema = self._load_schema()
        self.definition = self._find_definition()

        if self.definition is None:
            raise ValueError(f"Component '{component_id}' not found in schema")

        self.shl_type = self.definition.get("shl_type")
        self.text_keys = self.definition.get("text_keys", {})
        self.implementations = self.definition.get("implementations", {})
        self.metadata = self.definition.get("metadata", {})

    # -------------------------
    # Schema loading
    # -------------------------
    def _load_schema(self):
        if not os.path.exists(self.schema_path):
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        with open(self.schema_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _find_definition(self):
        for comp in self.schema.get("components", []):
            if comp.get("id") == self.component_id:
                return comp
        return None

    # -------------------------
    # Accessors
    # -------------------------
    def get_text_key(self, key_name):
        """Return the localization key for a given text field."""
        return self.text_keys.get(key_name)

    def get_framework_class(self, framework_name):
        """Return the UI class name for a given framework."""
        impl = self.implementations.get(framework_name)
        if impl:
            return impl.get("class")
        return None

    def supports(self, feature_name, framework_name):
        """Check if a framework implementation supports a specific feature."""
        impl = self.implementations.get(framework_name)
        if impl:
            return impl.get(feature_name, False)
        return False

    def requires_middleman(self):
        return self.metadata.get("middleman_required", False)

    def supports_language_manager(self):
        return self.metadata.get("supports_language_manager", True)

    def __repr__(self):
        return f"<SHLComponent id='{self.component_id}' type='{self.shl_type}'>"

