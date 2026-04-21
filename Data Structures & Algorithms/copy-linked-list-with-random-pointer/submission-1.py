"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = head
        while curr:
            copy = Node(x=curr.val)
            hashmap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr: 
            copy = hashmap[curr]
            print(copy.val)
            copy.next = hashmap[curr.next] if curr.next else None
            copy.random = hashmap[curr.random] if curr.random else None
            curr = curr.next
        
        return hashmap[head] if head else None

        