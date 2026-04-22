# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        heads = []
        for l in lists:
            heads.append(l)

        noneCount, n = 0, len(heads)
        while noneCount < n:
            minIdx, minVal = 101, 1001
            for i, h in enumerate(heads):
                if h is None:
                    continue
                else:
                    if h.val < minVal:
                        minIdx = i
                        minVal = h.val
            tail.next = heads[minIdx]
            tail = tail.next
            heads[minIdx] = heads[minIdx].next
            if heads[minIdx] is None:
                noneCount += 1

        return dummy.next    

                