# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail, carry = dummy, 0
        h1, h2 = l1, l2

        while h1 or h2:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            total = val1+val2+carry
            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next
            h1 = h1.next if h1 and h1.next else None
            h2 = h2.next if h2 and h2.next else None

        if carry:
            tail.next = ListNode(carry)

        return dummy.next