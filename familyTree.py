"""
Created by Jakub Adamczyk
Program is intended to make family trees
by interactive communication with user via console
"""


class Node:
    def __init__(self, name, parents, soName=None):
        self.name = name
        self.soName = soName
        self.parents = parents
        self.children = []

    def add_child(self, child):
        if type(child) == Node:
            self.children.append(child)

    def add_so(self, soName):
        if type(soName) == str:
            self.soName = soName

    def print_children(self):
        for child in self.children:
            print('{')
            print(child.name, child.soName)
            child.print_children()
            print('}')




class Tree:
    def __init__(self, name, soName):
        self.root = Node(name, None, soName)

    def print_tree(self):
        print(self.root.name, self.root.soName)
        self.root.print_children()


rodzina = Tree("Adam", "Ewa")
james = Node("James", rodzina.root, "Janet")
rodzina.root.add_child(james)
bartek = Node("Bartek", rodzina.root, "Helen")
rodzina.root.add_child(bartek)
jan = Node("Jan", bartek, "Maria")
bartek.add_child(jan)
peter = Node("Piotr", bartek, "Alice")
bartek.add_child(peter)

rodzina.print_tree()


