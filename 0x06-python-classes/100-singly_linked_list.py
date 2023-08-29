#!/usr/bin/python3
"""linked"""
class Node:
    """Node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if (isinstance(value, Node) or type(value) == None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        self.head = None
    def __str__(self):
        curr = self.head
        st = ""
        while curr != None:
            st += "{}\n".format(curr.data)
            curr = curr.next_node
        return (st)
    def sorted_insert(self, value):
        new = Node(value, None)
        curr = self.head
        if (curr == None):
            self.head = new
        elif (self.head.data >= value):
            new.next_node = self.head
            self.head = new
        else:
            while curr != None:
                if (curr.next_node == None):
                    curr.next_node = new
                    break
                if curr.next_node.data >= value:
                    new.next_node = curr.next_node
                    curr.next_node = new
                    break
                curr = curr.next_node
            
