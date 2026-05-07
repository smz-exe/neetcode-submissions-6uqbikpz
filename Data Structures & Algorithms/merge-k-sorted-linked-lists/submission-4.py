# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# pattern: divide and conquer
# data structure: linked list

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            if l1:
                tail.next = l1
            elif l2:
                tail.next = l2
            
            return dummy.next
        
        def divide(l: int, r: int) -> None:
            if l > r:
                return None
            
            if l == r:
                return lists[l]
            
            mid = l + (r - l) // 2

            left = divide(l, mid)
            right = divide(mid + 1, r)

            return merge(left, right)
        
        return divide(0, len(lists) - 1)