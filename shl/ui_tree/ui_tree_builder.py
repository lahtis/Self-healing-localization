"""
File: ui_tree_builder.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
UI tree construction interface: an abstract base class defining the build_tree method. 
Each adapter must implement this method to construct a UINode‑based UI tree from the blueprint, 
UCR, and healer‑produced data.

UI‑puun rakennusrajapinta: abstrakti perusluokka, joka määrittelee build_tree‑metodin. 
Jokaisen adapterin on toteutettava tämä metodi rakentaakseen UINode‑pohjaisen käyttöliittymäpuun blueprintin, 
UCR:n ja healerin tuottaman datan perusteella.
"""
class UITreeBuilder:
    def build_tree(self):
        """
        Returns a list of UINode objects representing the UI tree.
        Must be implemented by each adapter.
        """
        raise NotImplementedError

