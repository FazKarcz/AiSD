from typing import Any

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value: any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(node):
        wynik = node
        while (wynik.left is not None):
            wynik = wynik.left
        return wynik.value


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root) -> None:
        self.root = root

    def insert(self, value: any) -> None:


