class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        """
        Add a new node to the front of the list.

        Time Complexity: O(1)
        """
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

        return node

    def pop_tail(self):
        """
        Remove and return the value at the end of the list.

        Time Complexity: O(1)
        """
        if self.tail is None:
            return None

        node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = node.previous
            self.tail.next = None
            node.previous = None

        return node.value

    def remove(self, node):
        """
        Remove a node from the list.

        Time Complexity: O(1)
        """
        if node is None:
            return

        # Removing the head
        if node == self.head:
            self.head = node.next

        # Removing the tail
        if node == self.tail:
            self.tail = node.previous

        # Link previous node
        if node.previous is not None:
            node.previous.next = node.next

        # Link next node
        if node.next is not None:
            node.next.previous = node.previous

        # Disconnect node completely
        node.next = None
        node.previous = None