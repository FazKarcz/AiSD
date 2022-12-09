from __future__ import annotations
from typing import Any
import graphviz

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(node):
        minimum = node
        while(minimum.left is not None):
            minimum = minimum.left
        return minimum.value


class BinarySearchTree:
    root: BinaryNode

    def insert(self, value: Any) -> None:
        root = self._insert(self, value)
        self.root = root

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            node.left_child = node._insert(node.left_child, value)
        if value > node.value:
            node.right_child = node._insert(node.right_child, value)
        return node

    def insert_list(self, list_: list[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        node = self
        node.insert(value)
        if node == self:
            return True
        return False

    def remove(self, value: Any) -> None:
      print("holder")

    def _remove(self, node: BinaryNode,value: any):
      print("holder")

    def show():
      print("holder")


print("Działasz?")

drzewo = BinaryNode(25)
