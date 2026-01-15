"""
File: pyqt6_adapter.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
PyQt6 UI adapter for SHL: creates PyQt6 widgets from SHLComponent definitions, 
applies localized texts, and refreshes them on language change.

PyQt6‑UI‑adapteri SHL:lle: luo PyQt6‑widgetit SHLComponent‑määrittelyistä, 
asettaa lokalisoidut tekstit ja päivittää ne kielen vaihtuessa.
"""
from PyQt6 import QtWidgets
from shl.adapters.base import UIAdapter

class PyQt6Adapter(UIAdapter):
    """
    PyQt6 implementation of the SHL UI adapter.
    Creates PyQt6 widgets based on SHLComponent definitions.
    """

    # -------------------------
    # Widget creation
    # -------------------------
    def create_widget(self, component):
        widget_class = component.get_framework_class("PyQt6")

        if widget_class == "QLineEdit":
            widget = QtWidgets.QLineEdit()
        elif widget_class == "QPushButton":
            widget = QtWidgets.QPushButton()
        elif widget_class == "QComboBox":
            widget = QtWidgets.QComboBox()
        else:
            raise ValueError(f"Unsupported PyQt6 widget class: {widget_class}")

        # Apply initial localization
        self.apply_localization(widget, component)

        return widget

    # -------------------------
    # Text application
    # -------------------------
    def set_text(self, widget, component, field_name, text):
        """
        Applies localized text to the widget.
        PyQt6 supports label, placeholder and tooltip natively.
        """

        # Label text
        if field_name == "label":
            if hasattr(widget, "setText"):
                widget.setText(text)

        # Placeholder text
        if field_name == "placeholder":
            if hasattr(widget, "setPlaceholderText"):
                widget.setPlaceholderText(text)

        # Tooltip
        if field_name == "tooltip":
            widget.setToolTip(text)

    # -------------------------
    # Refresh on language change
    # -------------------------
    def refresh_widget(self, widget, component):
        """
        Reapply all localized texts to the widget.
        """
        self.apply_localization(widget, component)

