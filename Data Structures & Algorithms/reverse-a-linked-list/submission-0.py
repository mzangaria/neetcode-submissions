# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None 
        q = head
        
        while q: 
            temp = q.next
            q.next = pre
            pre = q
            q = temp
            
        
        return pre
