class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
    
    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_to_last(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert_to_last(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert_to_last(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
