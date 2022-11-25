from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return str(self.value)

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def is_leaf(self) -> bool:
        while self.left_child is None and self.right_child is None:
            return True
        return False

    #def traverse_in_order(self, visit: Callable[[Any], None]) -> None:

    #def traverse_post_order(self, visit: Callable[[Any], None]) -> None:

    #def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:


drzewo = BinaryNode(7)
drzewo.add_left_child(9)
drzewo.add_right_child(2)

print(drzewo)