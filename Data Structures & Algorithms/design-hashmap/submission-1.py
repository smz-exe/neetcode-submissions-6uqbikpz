class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: ListNode | None = None

class MyHashMap:
    BUCKET_COUNT = 1000

    def __init__(self):
        self.buckets: list[ListNode] = [ListNode(-1, -1) for _ in range(self.BUCKET_COUNT)]

    def put(self, key: int, value: int) -> None:
        index = key % self.BUCKET_COUNT
        cur = self.buckets[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            
            cur = cur.next
        
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.BUCKET_COUNT
        cur = self.buckets[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            
            cur = cur.next
        
        return -1

    def remove(self, key: int) -> None:
        index = key % self.BUCKET_COUNT
        cur = self.buckets[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)