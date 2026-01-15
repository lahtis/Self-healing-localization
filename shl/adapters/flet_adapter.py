"""
File: flet_adapter.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Flet UI adapter for SHL: creates Flet widgets from SHLComponent objects, 
applies values, and updates localization through the framework‑agnostic interface.

“Flet‑UI‑adapteri SHL:lle: luo Flet‑widgetit SHLComponent‑olioista,
asettaa arvot ja päivittää lokalisaation framework‑agnostisen rajapinnan kautta.
"""
import flet as ft
from shl.adapters.base import UIAdapter


class FletAdapter(UIAdapter):
    """
    Flet implementation of the SHL UI adapter.
    Creates Flet widgets based on SHLComponent definitions.
    """

    # ---------------------------------------------------------
    # Widget creation
    # ---------------------------------------------------------
    def create_widget(self, component):
        widget_class = component.get_framework_class("Flet")

        if widget_class == "TextField":
            widget = ft.TextField()

        elif widget_class == "ElevatedButton":
            # IMPORTANT: Flet buttons require content
            widget = ft.ElevatedButton(content=ft.Text(""))

        elif widget_class == "Dropdown":
            widget = ft.Dropdown()

        else:
            raise ValueError(f"Unsupported Flet widget class: {widget_class}")

        # Apply initial localization
        self.apply_localization(widget, component)

        return widget

    # ---------------------------------------------------------
    # Apply localized text
    # ---------------------------------------------------------
    def set_text(self, widget, component, field_name, text):
        # LABEL
        if field_name == "label":
            if isinstance(widget, ft.TextField):
                widget.label = text

            elif isinstance(widget, ft.ElevatedButton):
                # Päivitä olemassa oleva Text-olio
                if isinstance(widget.content, ft.Text):
                    widget.content.value = text
                else:
                    widget.content = ft.Text(text)

            elif isinstance(widget, ft.Dropdown):
                widget.label = text

        # PLACEHOLDER
        if field_name == "placeholder":
            if isinstance(widget, ft.TextField):
                widget.hint_text = text

        # TOOLTIP
        if field_name == "tooltip":
            widget.tooltip = text


    # ---------------------------------------------------------
    # Refresh widget on language change
    # ---------------------------------------------------------
    def refresh_widget(self, widget, component):
        self.apply_localization(widget, component)
        widget.update()

