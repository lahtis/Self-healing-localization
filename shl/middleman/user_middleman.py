"""
File: user_middleman.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Example implementation of the middleman layer: adapts a User object to SHL components (TEXT_INPUT and DROPDOWN), 
converts User data into UI‑friendly values, and maps UI values back into Python structures for form handling.

Esimerkkitoteutus middleman‑kerroksesta: sovittaa User‑olion SHL‑komponentteihin (TEXT_INPUT ja DROPDOWN),
muuntaa User‑datan UI‑arvoiksi ja palauttaa UI‑arvot takaisin Python‑rakenteiksi lomakkeiden käsittelyä varten.
"""
from shl.middleman.base import Middleman

class UserMiddleman(Middleman):
    """
    Example Middleman that adapts a User object to SHL UI components.
    """

    def supports(self, component):
        """
        This middleman supports:
            - TEXT_INPUT (e.g. name, email)
            - DROPDOWN (e.g. roles)
        """
        return component.shl_type in ["TEXT_INPUT", "DROPDOWN"]

    def to_component_value(self, component, user):
        """
        Converts a User object into a value suitable for the UI component.
        """

        # TEXT_INPUT → return a string
        if component.shl_type == "TEXT_INPUT":
            # Example: component.id = "user_name"
            if component.component_id == "user_name":
                return user.name
            if component.component_id == "user_email":
                return user.email

        # DROPDOWN → return a list of strings
        if component.shl_type == "DROPDOWN":
            if component.component_id == "user_role":
                return [role.name for role in user.roles]

        return None

    def from_component_value(self, component, value):
        """
        Converts UI value back into a Python data structure.
        Useful for forms and saving.
        """

        if component.shl_type == "TEXT_INPUT":
            return value  # raw string

        if component.shl_type == "DROPDOWN":
            return {"selected": value}

        return None

