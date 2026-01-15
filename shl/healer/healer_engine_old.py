"""
File: healer_engine_old.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
The original SHL healing engine: a simple text‑ and type‑based matcher that served as the 
foundation for the current heuristic and memory‑driven healing system. Preserved for historical reference.

SHL:n alkuperäinen healing‑moottori: yksinkertainen tekstin ja tyypin perusteella toimiva matcher, joka
toimi pohjana nykyiselle heuristiikka‑ ja muistipohjaiselle healing‑järjestelmälle. Säilytetään historiallisista syistä.
"""
from shl.healer.healer_logger import HealerLogger
from shl.healer.healer_log import HealerLogEntry
from shl.ui_tree.ui_tree_printer import UITreePrinter

class HealerEngine:
    def __init__(self, adapter, blueprint, logger=None):
        self.adapter = adapter
        self.blueprint = blueprint
        self.logger = logger or HealerLogger()

    # -----------------------------
    #  TEXT MATCHING
    # -----------------------------
    def _find_by_text(self, component, ui_tree):
        keys = []

        if hasattr(component, "user_key"):
            keys.append(component.user_key)

        for k in component.text_keys.values():
            keys.append(k)

        matches = []
        for node in ui_tree:
            if node.text:
                if any(key.lower() in node.text.lower() for key in keys):
                    matches.append(node)

        return matches

    # -----------------------------
    #  TYPE MATCHING
    # -----------------------------
    def _find_by_type(self, component, ui_tree):
        comp_type = component.type.lower()
        return [node for node in ui_tree if node.type.lower() == comp_type]

    # -----------------------------
    #  CONTEXT MATCHING
    # -----------------------------
    def _find_by_context(self, component, ui_tree):
        if not hasattr(component, "data_binding"):
            return []

        model = component.data_binding.get("model")
        if not model:
            return []

        related = [
            node for node in ui_tree
            if getattr(node, "data_model", None) == model
        ]

        return related

    # -----------------------------
    #  MAIN HEALING LOGIC
    # -----------------------------
    def repair_healer_key(self, component, ui_tree):
        old_key = component.healer_key

        # 1. TEXT MATCHING
        candidates = self._find_by_text(component, ui_tree)
        if len(candidates) == 1:
            new_key = candidates[0].selector
            self.logger.log(HealerLogEntry(
                component_id=component.id,
                old_key=old_key,
                new_key=new_key,
                reason="text_match",
                confidence=0.95
            ))
            return new_key

        # 2. TYPE MATCHING
        candidates = self._find_by_type(component, ui_tree)
        if len(candidates) == 1:
            new_key = candidates[0].selector
            self.logger.log(HealerLogEntry(
                component_id=component.id,
                old_key=old_key,
                new_key=new_key,
                reason="type_match",
                confidence=0.70
            ))
            return new_key

        # 3. CONTEXT MATCHING
        candidates = self._find_by_context(component, ui_tree)
        if len(candidates) == 1:
            new_key = candidates[0].selector
            self.logger.log(HealerLogEntry(
                component_id=component.id,
                old_key=old_key,
                new_key=new_key,
                reason="context_match",
                confidence=0.50
            ))
            return new_key

        return None

