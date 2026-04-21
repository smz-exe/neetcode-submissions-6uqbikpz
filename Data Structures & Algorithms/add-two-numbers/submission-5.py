# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail, h1, h2 = dummy, l1, l2
        carry = 0

        while h1 or h2:
            v1 = h1.val if h1 else 0
            v2 = h2.val if h2 else 0
            val = v1 + v2 + carry

            digit = val % 10
            carry = val // 10

            tail.next = ListNode(digit)
            tail = tail.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
        
        if carry:
            tail.next = ListNode(carry)
        
        return dummy.next