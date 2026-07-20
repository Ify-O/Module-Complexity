"""
Time Complexity

__init__  : O(1)
get()     : O(1)
set()     : O(1)

Space Complexity

O(n), where n is the cache limit.

Why?

- Dictionary provides O(1) key lookup.
- Doubly linked list provides O(1) insertion, removal, and moving nodes.
- No operation traverses the list.
""""""
Time Complexity

__init__  : O(1)
get()     : O(1)
set()     : O(1)

Space Complexity

O(n), where n is the cache limit.

Why?

- Dictionary provides O(1) key lookup.
- Doubly linked list provides O(1) insertion, removal, and moving nodes.
- No operation traverses the list.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LruCache:
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        self.limit = limit
        self.cache = {}

        self.head = None  # Most recently used
        self.tail = None  # Least recently used

    def _remove(self, node):
        if node.previous:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None

    def _add_to_head(self, node):
        node.previous = None
        node.next = self.head

        if self.head:
            self.head.previous = node

        self.head = node

        if self.tail is None:
            self.tail = node

    def get(self, key):
        node = self.cache.get(key)

        if node is None:
            return None

        # Move to the front (most recently used)
        self._remove(node)
        self._add_to_head(node)

        return node.value

    def set(self, key, value):
        # Update existing key
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
            return

        # Evict least recently used item if full
        if len(self.cache) >= self.limit:
            lru = self.tail
            self._remove(lru)
            del self.cache[lru.key]

        # Insert new item
        node = Node(key, value)
        self._add_to_head(node)
        self.cache[key] = node