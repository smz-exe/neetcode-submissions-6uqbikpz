# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt, curr = 0, head
        while curr:
            cnt += 1
            curr = curr.next
        
        dummy = ListNode()
        dummy.next, tail = head, dummy
        for _ in range(cnt - n):
            tail = tail.next
        temp = tail.next
        tail.next = temp.next
        return dummy.next

        