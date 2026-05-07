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
        
        def dfs(l: int, r: int):
            if l > r:
                return None

            if l == r:
                return lists[l]

            mid = l + (r - l) // 2

            left = dfs(l, mid)
            right = dfs(mid + 1, r)

            return merge(left, right)
        

        def merge(first: Optional[ListNode], second: Optional[ListNode]):
            dummy = ListNode()
            tail = dummy

            while first and second:
                if first.val < second.val:
                    tail.next = first
                    first = first.next
                else:
                    tail.next= second
                    second = second.next
                tail = tail.next
            
            if first:
                tail.next = first
            elif second:
                tail.next = second
            
            return dummy.next
        
        return dfs(0, len(lists) - 1)
