"""
Time Complexity

insert()      Average: O(log n)
contains()    Average: O(log n)
to_list()     O(n)

Space Complexity

O(n)

A skip list maintains multiple levels of linked lists,
allowing searches and insertions to skip over many nodes.
"""

import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    MAX_LEVEL = 6
    P = 0.5

    def __init__(self):
        self.level = 0
        self.head = Node(None, self.MAX_LEVEL)

    def random_level(self):
        level = 0
        while random.random() < self.P and level < self.MAX_LEVEL:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        # Find insertion position
        for i in range(self.level, -1, -1):
            while (
                current.forward[i] is not None
                and current.forward[i].value < value
            ):
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        # Ignore duplicates
        if current is not None and current.value == value:
            return

        new_level = self.random_level()

        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level

        new_node = Node(value, new_level)

        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def __contains__(self, value):
        current = self.head

        for i in range(self.level, -1, -1):
            while (
                current.forward[i] is not None
                and current.forward[i].value < value
            ):
                current = current.forward[i]

        current = current.forward[0]

        return current is not None and current.value == value

    def to_list(self):
        result = []
        current = self.head.forward[0]

        while current is not None:
            result.append(current.value)
            current = current.forward[0]

        return result