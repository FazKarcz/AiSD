from typing import Any,Callable,Union
import graphviz
from klass import Queue

class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []
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
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        pomocnicza = Queue()
        pomocnicza.enqueue(self)
        while (pomocnicza.len() > 0):
            wynik = pomocnicza.peek()
            pomocnicza.dequeue()
            visit(wynik)
            for i in range(len(wynik.children)):
                pomocnicza.enqueue(wynik.children[i])
    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for i in self.children:
            if i.value == value:
                i.search(value)
                return i
    def __str__(self) -> str:
        return str(self.value)
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
        self.root.for_each_deep_first(visit)
    def show(self):
        tree = graphviz.Digraph("drzewo")
        def add_tree(node: 'TreeNode'):
            for i in node.children:
                tree.edge(str(node.value),str(i.value))
        self.for_each_deep_first(add_tree)
        tree.view()

#TreeNode testing
drzewo = TreeNode(10)
el1 = TreeNode(9)
el2 = TreeNode(8)
el3 = TreeNode(5)
drzewo.add(el1)
drzewo.add(el2)
drzewo.add(el3)
#print(drzewo.is_leaf())
#drzewo.for_each_deep_first(print)
#drzewo.for_each_level_order(print)
#print(drzewo.search(8))


#Tree testing
korzen = TreeNode("J")
tree = Tree(korzen)
tree.add("E",korzen)
tree.add("B",korzen)
tree.add("D","E")
tree.add("Q","E")
tree.add("K","B")
tree.for_each_level_order(print)
print("///////////////////////////////////////////////////////////////////////////////")
tree.for_each_deep_first(print)
tree.show()
