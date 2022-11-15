from typing import Any, List, Callable, Union
import queue
class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []
    def __str__(self) -> str:
        return str(self.value)
#Sprzawdzanie czy węzeł jest liściem(czy nie jest "rodzicem")
    def is_leaf(self)->bool:
        if len(self.children) == 0:
            return True
        else:
            return False
    def add(self, child: 'TreeNode')->None:
        self.children.append(child)
    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)
    def for_each_level_order(self,visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        pomocnicza = queue.Queue()
        for i in self.children:
            pomocnicza.put(i)
            while pomocnicza.qsize() != 0:
                pomocnicza2 = pomocnicza.get(i)
                visit(pomocnicza2)
                for x in pomocnicza2.children:
                    pomocnicza.put(x)
    def search(self,value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for i in self.children:
            if i.value == value:
                i.search(value)
                return i
class Tree:
    root: TreeNode
    def __init__(self,value: any):
        self.root = TreeNode(value)
    def add(self,value: Any, parent_name: Any) -> None:
        pomocnicza = self.root.search(parent_name)
        pomocnicza.add(TreeNode(value))
    def for_each_level_order(self,visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)
    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)
#TreeNode testing
drzewo = TreeNode(10)
el1 = TreeNode(9)
el2 = TreeNode(8)
el3 = TreeNode(5)
drzewo.add(el1)
drzewo.add(el2)
#drzewo.for_each_deep_first(print)
#drzewo.for_each_level_order(print)
#print(drzewo.search(8))
#Tree testing
tree = Tree(10)
tree.add(5,10)
tree.add(9,5)
tree.for_each_level_order(print)
#tree.for_each_deep_first(print)


