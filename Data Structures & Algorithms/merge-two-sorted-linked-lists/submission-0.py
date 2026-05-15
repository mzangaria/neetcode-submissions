# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res, last = None, None
        p1, p2 = list1, list2

        if not p1:
            return p2
        
        if not p2:
            return p1
            
        if p1.val > p2.val:
            res = last = p2
            p2 = p2.next
        else:
            res = last = p1
            p1 = p1.next
        
        while p1 or p2:
            if not p1:
                last.next = p2
                break
            if not p2:
                last.next = p1
                break
            
            if p1.val > p2.val:
                last.next = p2
                p2 = p2.next
            else:
                last.next = p1
                p1 = p1.next
            last = last.next
        
        return res

