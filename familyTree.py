'''
Created by Jakub Adamczyk
Program is intended to make family trees
by interactive communication with user via console
'''
class Node:
"""
Class for creating node objects that will store data and connection pointers
"""
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.couple = None
        self.parentM = None
        self.partentK = None


class Tree:
    """
    Class that holds our tree, has functions, and knows where the root exactly is
    """
    def __init__(self)
