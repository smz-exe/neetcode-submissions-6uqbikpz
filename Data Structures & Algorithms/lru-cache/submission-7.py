# I'll use a hashmap from key to node, and a doubly linked list to maintain recency order.
# The left dummy points to the least recently used node, and the right dummy represents the most recently used side.
# On every get, I move the accessed node to the MRU side.
# On put, I update or insert the node, move it to MRU, and evict from the LRU side if capacity is exceeded.
# This gives O(1) time for both operations.

class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.val = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None 


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}

        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _insert_mru(self, node: Node) -> None:
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_mru(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self._insert_mru(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
        