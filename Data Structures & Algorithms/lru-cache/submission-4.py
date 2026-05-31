class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}

        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_to_mru(self, node: Node) -> None:
        prev_node = self.right.prev
        next_node =  self.right

        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert_to_mru(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_to_mru(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self._insert_to_mru(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
