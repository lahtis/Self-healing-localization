"""
File: ui_node.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
UI node base model: represents a single node in the UI tree, including its type, text, selector, and children. 
Provides the structural unit used by middleman, healer, and adapters to build, modify, and render the UI tree.

UI‑solmun perusmalli: kuvaa käyttöliittymäpuun yksittäisen solmun, sen tyypin, tekstin, valitsimen ja lapsisolmut. 
Tarjoaa rakenteen, jota middleman, healer ja adapterit käyttävät UI‑puun rakentamiseen, muokkaamiseen ja renderöintiin.
"""
from dataclasses import dataclass, field

@dataclass
class UINode:
    id: str | None
    type: str
    text: str | None
    selector: str | None
    children: list = field(default_factory=list)

    def add_child(self, node):
        self.children.append(node)

