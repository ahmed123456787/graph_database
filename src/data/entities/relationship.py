from dataclasses import dataclass
from typing import List,Optional
from node import Node


@dataclass
class RelationshipType:
    """Represents the type of a relationship in a graph database."""
    value:str


@dataclass
class Relationship:
    """Represents a relationship between two nodes in a graph database."""
    src_node:Node
    target_node:Node
    rel_type:RelationshipType
    properties:Optional[dict] = None
