"""
File: base.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Abstract base class for SHL UI adapters: defines widget creation, 
text application, and localization refresh logic.

“SHL:n UI‑adapterien abstrakti pohjaluokka: määrittelee widgetin luonnin, 
tekstien asettamisen ja lokalisaation päivityksen.
"""
from abc import ABC, abstractmethod

class UIAdapter(ABC):
    """
    Base class for all UI framework adapters.
    A UIAdapter knows how to:
        - Create a concrete UI widget from an SHLComponent
        - Apply localized texts from LanguageManager
        - Update the widget when language changes
    """

    def __init__(self, language_manager):
        self.language_manager = language_manager

    # -------------------------
    # Required methods
    # -------------------------
    @abstractmethod
    def create_widget(self, component):
        """
        Creates a concrete UI widget for the given SHLComponent.
        Must return a framework-specific widget instance.
        """
        pass

    @abstractmethod
    def set_text(self, widget, component, field_name, text):
        """
        Applies a localized text to a specific field of the widget.
        Example:
            field_name = "label"
            text = "Save"
        """
        pass

    @abstractmethod
    def refresh_widget(self, widget, component):
        """
        Called when the language changes.
        Should reapply all localized texts to the widget.
        """
        pass

    # -------------------------
    # Helper method
    # -------------------------
    def apply_localization(self, widget, component):
        """
        Applies all localized texts from LanguageManager to the widget.
        """
        texts = self.language_manager.get_component_texts(component)

        for field_name, text in texts.items():
            self.set_text(widget, component, field_name, text)

