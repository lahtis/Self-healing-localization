"""
File: ucr_loader.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
UCR registry loader: reads a Universal Component Registry file, validates it against the UCR schema, and constructs
SHLComponent objects including text_keys, framework_map definitions, and optional data_binding configuration.

UCR‑rekisterin latausmoduuli: lukee Universal Component Registry ‑tiedoston, validoi sen UCR‑skeemaa
vasten ja rakentaa siitä SHLComponent‑oliot, mukaan lukien text_keys‑arvot, framework_map‑määritykset 
ja mahdollisen data_binding‑konfiguraation.
"""
import json
from pathlib import Path
from shl.ui.components.SHLComponent import SHLComponent
from shl.registry.ucr_validator import validate_ucr


def load_ucr(path: str | Path):
    """
    Loads a UCR (Universal Component Registry) JSON file and
    returns a list of SHLComponent objects.
    """

    path = Path(path)
    validate_ucr(path, Path(__file__).parent / "ucr_schema.json")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    components = []

    for comp_id, comp_data in data.get("components", {}).items():
        component = SHLComponent(comp_id)

        # Attach text keys (label, placeholder, tooltip…)
        if "text_keys" in comp_data:
            for key, value in comp_data["text_keys"].items():
                component.text_keys[key] = value

        # Attach framework mapping (Flet, PyQt, Playwright…)
        if "framework_map" in comp_data:
            for fw, fw_data in comp_data["framework_map"].items():
                component.framework_map[fw] = fw_data

        # Attach data binding (optional)
        if "data_binding" in comp_data:
            component.data_binding = comp_data["data_binding"]

        components.append(component)

    return components

