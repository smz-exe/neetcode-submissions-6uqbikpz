class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set: list[ListNode] = [ListNode(-1) for i in range(1000)]

    def add(self, key: int) -> None:
        index = key % 1000
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % 1000
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % 1000
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True

            cur = cur.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)