from dataclasses import dataclass
from typing import List

@dataclass
class NodeLabel:
    value:str


@dataclass
class Node:
    id: int
    label: List[NodeLabel]
    properties: dict


    def add_property(self, key: str, value):
        self.properties[key] = value

    def get_property(self, key: str):
        return self.properties.get(key)
    
    def __str__(self):
        return f"Node(id={self.id}, label={self.label.value}, properties={self.properties})"